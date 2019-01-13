# Monoprice Monolith M1060
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 4.3; 28 4.3; 31 4.4; 34 4.4; 37 4.3; 41 3.9; 45 3.3; 49 3.0; 54 3.0; 60 2.9; 66 2.8; 72 2.6; 79 2.4; 87 2.0; 96 1.5; 106 1.3; 116 1.1; 128 0.8; 141 0.5; 155 0.4; 170 0.1; 187 -0.1; 206 -0.4; 227 -0.3; 249 -0.3; 274 0.1; 302 0.1; 332 0.0; 365 0.5; 402 0.9; 442 0.8; 486 0.4; 535 0.1; 588 -0.0; 647 -0.4; 712 -0.6; 783 -0.2; 861 0.5; 947 0.1; 1042 0.3; 1146 -0.2; 1261 -0.5; 1387 -0.7; 1526 -1.6; 1678 -0.8; 1846 1.4; 2031 2.8; 2234 3.3; 2457 2.7; 2703 2.9; 2973 3.8; 3270 3.3; 3597 3.5; 3957 2.9; 4353 6.0; 4788 5.3; 5267 6.0; 5793 6.0; 6373 4.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.3; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Monolith M1060 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Monolith M1060 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.49 | 4.5 dB  |
| Peaking | 1153 Hz | 0.84 | -0.7 dB |
| Peaking | 1559 Hz | 3.3  | -3.7 dB |
| Peaking | 2238 Hz | 0.93 | 3.5 dB  |
| Peaking | 5217 Hz | 2.03 | 5.9 dB  |
| Peaking | 214 Hz  | 2.43 | -0.8 dB |
| Peaking | 420 Hz  | 3.97 | 1.0 dB  |
| Peaking | 684 Hz  | 7.02 | -0.8 dB |
| Peaking | 6556 Hz | 4.28 | 2.7 dB  |
| Peaking | 7593 Hz | 1.97 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%20Monolith%20M1060/Monoprice%20Monolith%20M1060.png)