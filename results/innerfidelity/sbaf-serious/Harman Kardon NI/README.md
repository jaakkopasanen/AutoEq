# Harman Kardon NI
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.3; 28 -8.3; 31 -8.2; 34 -8.1; 37 -8.0; 41 -7.9; 45 -7.8; 49 -7.7; 54 -7.6; 60 -7.5; 66 -7.4; 72 -7.3; 79 -7.3; 87 -7.2; 96 -7.1; 106 -6.9; 116 -6.6; 128 -6.4; 141 -6.2; 155 -5.8; 170 -5.5; 187 -5.1; 206 -4.7; 227 -4.1; 249 -3.7; 274 -3.2; 302 -2.8; 332 -2.3; 365 -1.8; 402 -1.3; 442 -0.8; 486 -0.6; 535 -0.2; 588 0.3; 647 0.5; 712 0.4; 783 0.5; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.3; 1387 -2.3; 1526 -3.3; 1678 -4.3; 1846 -5.2; 2031 -6.1; 2234 -7.5; 2457 -9.1; 2703 -9.3; 2973 -6.0; 3270 -2.5; 3597 -0.7; 3957 -1.4; 4353 -4.8; 4788 -9.0; 5267 -11.3; 5793 -3.8; 6373 1.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.6; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Harman Kardon NI GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Harman Kardon NI ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.1  | -8.1 dB  |
| Peaking | 625 Hz  | 1.1  | 1.9 dB   |
| Peaking | 2385 Hz | 1.96 | -9.1 dB  |
| Peaking | 5168 Hz | 5    | -12.7 dB |
| Peaking | 6639 Hz | 3.87 | 4.8 dB   |
| Peaking | 1701 Hz | 2.16 | -3.6 dB  |
| Peaking | 2082 Hz | 1.15 | 3.1 dB   |
| Peaking | 2755 Hz | 4.85 | -4.1 dB  |
| Peaking | 3643 Hz | 3.73 | 2.8 dB   |
| Peaking | 4542 Hz | 5.54 | -2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Harman%20Kardon%20NI/Harman%20Kardon%20NI.png)