# Monster Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 -11.4; 23 -11.3; 25 -11.2; 28 -11.0; 31 -10.9; 34 -10.7; 37 -10.6; 41 -10.4; 45 -10.2; 49 -10.0; 54 -9.8; 60 -9.6; 66 -9.4; 72 -9.3; 79 -9.2; 87 -9.1; 96 -8.9; 106 -8.6; 116 -8.3; 128 -8.0; 141 -7.7; 155 -7.3; 170 -6.9; 187 -6.4; 206 -5.9; 227 -5.2; 249 -4.8; 274 -4.2; 302 -3.6; 332 -3.1; 365 -2.4; 402 -1.9; 442 -1.2; 486 -0.9; 535 -0.4; 588 0.3; 647 0.6; 712 0.8; 783 1.0; 861 0.7; 947 0.3; 1042 -0.4; 1146 -0.5; 1261 -1.1; 1387 -1.5; 1526 -2.4; 1678 -3.3; 1846 -4.0; 2031 -4.5; 2234 -5.3; 2457 -5.8; 2703 -6.0; 2973 -4.6; 3270 -2.6; 3597 -1.4; 3957 -2.3; 4353 -5.1; 4788 -5.8; 5267 -2.9; 5793 0.9; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.0; 10263 -2.3; 11289 -2.0; 12418 -0.9; 13660 -2.2; 15026 -0.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.21 | -11.0 dB |
| Peaking | 155 Hz   | 0.8  | -3.7 dB  |
| Peaking | 2397 Hz  | 1.78 | -6.1 dB  |
| Peaking | 4712 Hz  | 4.6  | -6.0 dB  |
| Peaking | 6458 Hz  | 5.21 | 5.2 dB   |
| Peaking | 740 Hz   | 2.06 | 1.9 dB   |
| Peaking | 1691 Hz  | 3.28 | -1.4 dB  |
| Peaking | 2820 Hz  | 1.83 | 2.1 dB   |
| Peaking | 2853 Hz  | 4.69 | -3.1 dB  |
| Peaking | 11685 Hz | 1.71 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)