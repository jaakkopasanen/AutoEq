# Sony WF-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.5; 28 3.4; 31 3.4; 34 3.4; 37 3.4; 41 3.3; 45 3.2; 49 3.1; 54 2.8; 60 2.3; 66 1.8; 72 1.3; 79 0.8; 87 0.2; 96 -0.4; 106 -1.1; 116 -1.6; 128 -2.1; 141 -2.4; 155 -2.8; 170 -2.9; 187 -3.1; 206 -3.0; 227 -2.7; 249 -2.5; 274 -2.4; 302 -2.5; 332 -2.7; 365 -2.9; 402 -3.1; 442 -3.0; 486 -2.8; 535 -2.5; 588 -2.1; 647 -1.5; 712 -1.0; 783 -0.6; 861 -0.2; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.3; 1526 1.2; 1678 0.3; 1846 -1.3; 2031 -2.2; 2234 -2.2; 2457 -1.7; 2703 -0.8; 2973 0.2; 3270 0.5; 3597 0.4; 3957 0.3; 4353 0.1; 4788 0.4; 5267 0.1; 5793 -0.7; 6373 -1.6; 7010 0.3; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -6.8; 11289 -7.9; 12418 -3.7; 13660 -0.0; 15026 0.0; 16529 0.0; 18182 -1.9; 20000 -1.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.33 | 4.0 dB  |
| Peaking | 152 Hz   | 0.68 | -4.1 dB |
| Peaking | 446 Hz   | 1.62 | -2.4 dB |
| Peaking | 2170 Hz  | 4.62 | -2.6 dB |
| Peaking | 10997 Hz | 4.18 | -9.2 dB |
| Peaking | 935 Hz   | 9.14 | 1.0 dB  |
| Peaking | 3477 Hz  | 3.9  | 0.7 dB  |
| Peaking | 6435 Hz  | 5.09 | -3.1 dB |
| Peaking | 7046 Hz  | 2.28 | 2.2 dB  |
| Peaking | 19142 Hz | 2.87 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WF-1000X/Sony%20WF-1000X.png)