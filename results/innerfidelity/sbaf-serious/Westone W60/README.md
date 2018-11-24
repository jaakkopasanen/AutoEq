# Westone W60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.0; 23 -0.2; 25 -0.3; 28 -0.5; 31 -0.6; 34 -0.7; 37 -0.8; 41 -1.0; 45 -1.2; 49 -1.4; 54 -1.6; 60 -1.9; 66 -2.2; 72 -2.5; 79 -2.8; 87 -3.2; 96 -3.6; 106 -3.8; 116 -4.0; 128 -4.2; 141 -4.4; 155 -4.5; 170 -4.5; 187 -4.5; 206 -4.4; 227 -4.2; 249 -4.1; 274 -3.8; 302 -3.5; 332 -3.2; 365 -2.9; 402 -2.5; 442 -2.0; 486 -1.7; 535 -1.3; 588 -0.6; 647 -0.2; 712 0.0; 783 0.5; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -1.0; 1387 -1.8; 1526 -2.4; 1678 -2.3; 1846 -1.2; 2031 0.8; 2234 3.2; 2457 5.3; 2703 5.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.6; 10263 -3.4; 11289 -0.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 113 Hz  | 0.63 | -2.2 dB |
| Peaking | 249 Hz  | 0.53 | -3.4 dB |
| Peaking | 1616 Hz | 1.5  | -8.5 dB |
| Peaking | 3204 Hz | 0.37 | 8.1 dB  |
| Peaking | 9691 Hz | 1.69 | -5.9 dB |
| Peaking | 2015 Hz | 5.25 | -1.0 dB |
| Peaking | 2509 Hz | 2.78 | 1.5 dB  |
| Peaking | 3871 Hz | 1.22 | -1.2 dB |
| Peaking | 6577 Hz | 1.92 | 2.4 dB  |
| Peaking | 7436 Hz | 5.31 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W60/Westone%20W60.png)