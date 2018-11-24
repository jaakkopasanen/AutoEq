# Sony MDR-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -5.2; 23 -4.9; 25 -4.6; 28 -4.4; 31 -4.1; 34 -4.0; 37 -3.8; 41 -3.7; 45 -3.6; 49 -3.7; 54 -3.8; 60 -4.0; 66 -4.2; 72 -4.3; 79 -4.5; 87 -4.7; 96 -4.9; 106 -5.2; 116 -5.4; 128 -5.6; 141 -5.6; 155 -5.3; 170 -4.9; 187 -4.6; 206 -4.2; 227 -3.7; 249 -3.5; 274 -3.5; 302 -3.1; 332 -2.4; 365 -1.7; 402 -1.6; 442 -2.1; 486 -2.0; 535 -1.7; 588 -0.4; 647 -1.1; 712 -2.8; 783 -2.3; 861 -0.9; 947 -0.7; 1042 0.7; 1146 2.7; 1261 2.2; 1387 0.5; 1526 -2.3; 1678 -3.6; 1846 -4.0; 2031 -3.2; 2234 -1.9; 2457 -0.2; 2703 0.9; 2973 1.1; 3270 2.3; 3597 2.6; 3957 -0.6; 4353 -3.4; 4788 -2.6; 5267 -2.3; 5793 -1.6; 6373 0.4; 7010 2.2; 7711 -0.3; 8482 -3.0; 9330 -1.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 1.08 | -5.0 dB |
| Peaking | 24 Hz    | 0.75 | -2.4 dB |
| Peaking | 132 Hz   | 0.48 | -5.2 dB |
| Peaking | 1831 Hz  | 4.79 | -4.6 dB |
| Peaking | 21788 Hz | 2.22 | -1.1 dB |
| Peaking | 1188 Hz  | 2.82 | 7.1 dB  |
| Peaking | 1201 Hz  | 1.1  | -3.7 dB |
| Peaking | 3662 Hz  | 2.15 | 5.7 dB  |
| Peaking | 4318 Hz  | 2.94 | -6.8 dB |
| Peaking | 8698 Hz  | 8.52 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-1000X/Sony%20MDR-1000X.png)