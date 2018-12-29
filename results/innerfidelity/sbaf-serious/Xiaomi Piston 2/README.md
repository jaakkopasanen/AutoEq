# Xiaomi Piston 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -9.6; 23 -9.7; 25 -9.9; 28 -10.1; 31 -10.2; 34 -10.2; 37 -10.3; 41 -10.3; 45 -10.4; 49 -10.4; 54 -10.4; 60 -10.5; 66 -10.5; 72 -10.6; 79 -10.7; 87 -10.7; 96 -10.7; 106 -10.6; 116 -10.3; 128 -10.2; 141 -10.0; 155 -9.7; 170 -9.2; 187 -8.8; 206 -8.4; 227 -7.8; 249 -7.2; 274 -6.6; 302 -6.0; 332 -5.3; 365 -4.7; 402 -4.0; 442 -3.2; 486 -2.7; 535 -2.1; 588 -1.2; 647 -0.7; 712 -0.3; 783 0.2; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -1.1; 1526 -1.6; 1678 -1.9; 1846 -2.0; 2031 -1.9; 2234 -1.9; 2457 -1.6; 2703 -1.6; 2973 -1.0; 3270 0.1; 3597 0.8; 3957 -0.0; 4353 -2.4; 4788 -3.9; 5267 -5.1; 5793 -6.2; 6373 -5.2; 7010 -3.0; 7711 -2.2; 8482 -3.3; 9330 -4.6; 10263 -3.4; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Piston 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.23 | -10.0 dB |
| Peaking | 180 Hz   | 0.66 | -4.6 dB  |
| Peaking | 1911 Hz  | 2.99 | -1.8 dB  |
| Peaking | 6098 Hz  | 1.58 | -5.6 dB  |
| Peaking | 24000 Hz | 2.11 | -2.6 dB  |
| Peaking | 821 Hz   | 2.46 | 1.5 dB   |
| Peaking | 3698 Hz  | 2.97 | 5.0 dB   |
| Peaking | 3918 Hz  | 1.16 | -2.6 dB  |
| Peaking | 7179 Hz  | 4.26 | 2.4 dB   |
| Peaking | 9484 Hz  | 5.38 | -3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%202/Xiaomi%20Piston%202.png)