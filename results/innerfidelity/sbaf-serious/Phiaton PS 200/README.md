# Phiaton PS 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.6; 28 3.5; 31 3.4; 34 3.4; 37 3.3; 41 3.1; 45 2.9; 49 2.8; 54 2.6; 60 2.3; 66 2.0; 72 1.7; 79 1.3; 87 0.9; 96 0.4; 106 0.1; 116 -0.1; 128 -0.5; 141 -0.8; 155 -0.9; 170 -1.0; 187 -1.2; 206 -1.4; 227 -1.2; 249 -1.3; 274 -1.2; 302 -1.1; 332 -1.0; 365 -0.8; 402 -0.7; 442 -0.4; 486 -0.3; 535 -0.1; 588 0.4; 647 0.5; 712 0.5; 783 0.8; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -1.2; 1526 -1.8; 1678 -2.1; 1846 -2.0; 2031 -1.8; 2234 -1.2; 2457 0.6; 2703 2.7; 2973 5.6; 3270 6.0; 3597 6.0; 3957 5.7; 4353 2.4; 4788 0.5; 5267 -0.3; 5793 -0.8; 6373 -0.5; 7010 0.5; 7711 0.3; 8482 -0.0; 9330 -2.0; 10263 -4.4; 11289 -1.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.19 | 3.8 dB  |
| Peaking | 51 Hz    | 1.95 | 2.1 dB  |
| Peaking | 1908 Hz  | 1.81 | -3.1 dB |
| Peaking | 3336 Hz  | 2.39 | 7.5 dB  |
| Peaking | 10243 Hz | 5.27 | -4.9 dB |
| Peaking | 232 Hz   | 1    | -1.5 dB |
| Peaking | 764 Hz   | 2.32 | 1.1 dB  |
| Peaking | 3986 Hz  | 9.47 | 2.4 dB  |
| Peaking | 5860 Hz  | 1.93 | -2.3 dB |
| Peaking | 7087 Hz  | 2.45 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20200/Phiaton%20PS%20200.png)