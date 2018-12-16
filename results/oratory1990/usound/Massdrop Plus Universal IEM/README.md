# Massdrop Plus Universal IEM

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 21 -1.3; 23 -1.4; 25 -1.5; 28 -1.6; 31 -1.7; 34 -1.7; 37 -1.8; 41 -1.9; 45 -2.1; 49 -2.2; 54 -2.4; 60 -2.5; 66 -2.8; 72 -3.0; 79 -3.3; 87 -3.6; 96 -3.8; 106 -4.0; 116 -4.2; 128 -4.3; 141 -4.4; 155 -4.4; 170 -4.3; 187 -4.1; 206 -3.9; 227 -3.6; 249 -3.3; 274 -3.0; 302 -2.6; 332 -2.2; 365 -1.8; 402 -1.5; 442 -1.3; 486 -1.0; 535 -0.7; 588 -0.4; 647 -0.1; 712 0.2; 783 0.5; 861 0.5; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.8; 1387 -2.5; 1526 -3.1; 1678 -3.4; 1846 -3.6; 2031 -3.8; 2234 -3.9; 2457 -3.6; 2703 -3.0; 2973 -2.4; 3270 -2.0; 3597 -1.8; 3957 -1.7; 4353 -1.6; 4788 -1.0; 5267 0.2; 5793 1.1; 6373 0.8; 7010 -2.1; 7711 -4.8; 8482 -3.6; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.6; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus Universal IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus Universal IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 49 Hz    | 0.41 | -1.7 dB |
| Peaking | 135 Hz   | 0.89 | -3.3 dB |
| Peaking | 252 Hz   | 1.49 | -1.7 dB |
| Peaking | 2126 Hz  | 1.31 | -4.2 dB |
| Peaking | 7896 Hz  | 6.2  | -5.4 dB |
| Peaking | 858 Hz   | 2.42 | 1.4 dB  |
| Peaking | 1426 Hz  | 4.15 | -1.0 dB |
| Peaking | 4254 Hz  | 3.21 | -0.9 dB |
| Peaking | 5910 Hz  | 4.98 | 2.2 dB  |
| Peaking | 14902 Hz | 8    | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Massdrop%20Plus%20Universal%20IEM/Massdrop%20Plus%20Universal%20IEM.png)