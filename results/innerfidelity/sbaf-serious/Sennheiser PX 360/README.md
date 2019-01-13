# Sennheiser PX 360
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.7; 49 5.2; 54 4.7; 60 4.0; 66 3.4; 72 2.9; 79 2.2; 87 1.5; 96 1.0; 106 0.8; 116 0.5; 128 0.7; 141 1.6; 155 2.1; 170 1.9; 187 3.5; 206 2.1; 227 1.2; 249 0.5; 274 0.4; 302 0.6; 332 0.0; 365 0.4; 402 1.1; 442 1.7; 486 1.5; 535 1.7; 588 2.1; 647 1.8; 712 1.6; 783 1.5; 861 1.1; 947 0.6; 1042 -0.4; 1146 -1.6; 1261 -3.0; 1387 -4.7; 1526 -6.5; 1678 -7.9; 1846 -8.7; 2031 -7.8; 2234 -5.8; 2457 -2.8; 2703 -0.8; 2973 1.0; 3270 2.9; 3597 5.0; 3957 6.0; 4353 3.7; 4788 2.9; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -2.4; 11289 -1.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 360 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.57 | 6.4 dB   |
| Peaking | 777 Hz   | 0.66 | 2.8 dB   |
| Peaking | 1802 Hz  | 1.43 | -10.5 dB |
| Peaking | 3684 Hz  | 2.19 | 6.8 dB   |
| Peaking | 5872 Hz  | 3.76 | 6.1 dB   |
| Peaking | 105 Hz   | 3.02 | -1.2 dB  |
| Peaking | 186 Hz   | 4.89 | 2.7 dB   |
| Peaking | 334 Hz   | 4.19 | -1.0 dB  |
| Peaking | 9841 Hz  | 0.57 | 0.3 dB   |
| Peaking | 10278 Hz | 3.36 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)