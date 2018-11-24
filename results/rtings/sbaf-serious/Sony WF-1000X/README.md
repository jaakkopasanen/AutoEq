# Sony WF-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 0.0; 23 3.8; 25 3.7; 28 3.6; 31 3.5; 34 3.4; 37 3.3; 41 3.1; 45 2.9; 49 2.7; 54 2.5; 60 2.0; 66 1.6; 72 1.3; 79 1.0; 87 0.5; 96 0.0; 106 -0.6; 116 -1.1; 128 -1.6; 141 -1.9; 155 -2.1; 170 -2.3; 187 -2.5; 206 -2.5; 227 -2.2; 249 -1.9; 274 -1.7; 302 -1.7; 332 -1.8; 365 -1.9; 402 -2.0; 442 -1.9; 486 -1.6; 535 -1.3; 588 -1.0; 647 -0.5; 712 -0.1; 783 -0.1; 861 -0.0; 947 0.4; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -1.3; 1526 0.8; 1678 -0.0; 1846 -1.2; 2031 -1.8; 2234 -1.7; 2457 -1.3; 2703 0.0; 2973 1.8; 3270 3.1; 3597 3.6; 3957 2.7; 4353 1.4; 4788 2.0; 5267 3.1; 5793 3.2; 6373 2.2; 7010 2.4; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -5.1; 11289 -2.6; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.24 | 4.3 dB  |
| Peaking | 158 Hz   | 0.46 | -4.1 dB |
| Peaking | 3535 Hz  | 4.86 | 3.6 dB  |
| Peaking | 5782 Hz  | 2.34 | 3.3 dB  |
| Peaking | 10428 Hz | 5.48 | -6.0 dB |
| Peaking | 425 Hz   | 4.92 | -0.6 dB |
| Peaking | 523 Hz   | 2.78 | -0.4 dB |
| Peaking | 775 Hz   | 2.71 | 0.5 dB  |
| Peaking | 1480 Hz  | 0.14 | 0.2 dB  |
| Peaking | 2154 Hz  | 3.44 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WF-1000X/Sony%20WF-1000X.png)