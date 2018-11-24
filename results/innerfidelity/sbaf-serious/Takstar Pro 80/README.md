# Takstar Pro 80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.3; 28 1.9; 31 1.6; 34 1.4; 37 1.3; 41 1.2; 45 1.1; 49 1.0; 54 0.8; 60 0.8; 66 0.6; 72 0.5; 79 0.3; 87 -0.0; 96 -0.2; 106 -0.2; 116 -0.4; 128 -0.9; 141 -1.5; 155 -1.3; 170 -1.1; 187 -1.4; 206 -1.3; 227 -1.1; 249 -0.9; 274 -0.6; 302 -0.2; 332 0.3; 365 0.8; 402 1.5; 442 2.1; 486 2.0; 535 1.9; 588 1.9; 647 1.4; 712 0.9; 783 0.9; 861 1.3; 947 0.5; 1042 -0.0; 1146 -0.4; 1261 -1.2; 1387 -1.9; 1526 -3.0; 1678 -3.5; 1846 -3.9; 2031 -3.7; 2234 -2.2; 2457 0.6; 2703 3.4; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 2.8; 5267 4.1; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.2; 9330 -4.2; 10263 -2.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Takstar Pro 80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Takstar Pro 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.08 | 2.8 dB   |
| Peaking | 1955 Hz | 1.12 | -16.3 dB |
| Peaking | 2615 Hz | 0.54 | 13.5 dB  |
| Peaking | 6228 Hz | 6.25 | 2.9 dB   |
| Peaking | 9217 Hz | 2.48 | -6.6 dB  |
| Peaking | 196 Hz  | 1.09 | -1.7 dB  |
| Peaking | 474 Hz  | 1.86 | 1.9 dB   |
| Peaking | 1306 Hz | 3.3  | -0.9 dB  |
| Peaking | 4760 Hz | 2.47 | 1.7 dB   |
| Peaking | 4940 Hz | 8.37 | -4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Takstar%20Pro%2080/Takstar%20Pro%2080.png)