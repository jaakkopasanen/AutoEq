# Sennheiser RS 185

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.0; 28 -0.7; 31 -1.2; 34 -1.7; 37 -2.0; 41 -2.3; 45 -2.5; 49 -2.6; 54 -2.7; 60 -2.9; 66 -3.1; 72 -3.3; 79 -3.5; 87 -3.7; 96 -3.9; 106 -4.3; 116 -4.6; 128 -4.8; 141 -5.1; 155 -5.1; 170 -5.2; 187 -5.1; 206 -5.0; 227 -4.9; 249 -4.7; 274 -4.4; 302 -4.1; 332 -3.9; 365 -3.6; 402 -3.4; 442 -3.1; 486 -2.8; 535 -1.5; 588 -0.5; 647 -0.3; 712 -0.6; 783 -0.6; 861 1.0; 947 0.2; 1042 -0.3; 1146 -0.4; 1261 -0.7; 1387 -0.9; 1526 -0.7; 1678 -0.8; 1846 -0.8; 2031 -1.0; 2234 -2.8; 2457 -5.4; 2703 -6.6; 2973 -6.9; 3270 -6.0; 3597 -3.4; 3957 -2.1; 4353 -1.9; 4788 1.1; 5267 4.2; 5793 4.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -1.9; 10263 -1.9; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 185 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 185 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 115 Hz  | 0.5  | -4.0 dB |
| Peaking | 267 Hz  | 0.95 | -2.6 dB |
| Peaking | 2958 Hz | 2.19 | -7.6 dB |
| Peaking | 5972 Hz | 2.69 | 6.3 dB  |
| Peaking | 9594 Hz | 3.75 | -2.7 dB |
| Peaking | 20 Hz   | 2.69 | 1.9 dB  |
| Peaking | 460 Hz  | 3.01 | -1.7 dB |
| Peaking | 641 Hz  | 1.11 | 1.1 dB  |
| Peaking | 2049 Hz | 5    | 1.2 dB  |
| Peaking | 2455 Hz | 5.82 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20RS%20185/Sennheiser%20RS%20185.png)