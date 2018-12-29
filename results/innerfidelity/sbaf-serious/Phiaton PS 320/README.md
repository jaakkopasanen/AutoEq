# Phiaton PS 320
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.2; 25 2.0; 28 1.9; 31 1.7; 34 1.6; 37 1.6; 41 1.5; 45 1.3; 49 1.0; 54 0.8; 60 0.6; 66 0.4; 72 0.7; 79 0.7; 87 -0.2; 96 -1.2; 106 -2.2; 116 -2.3; 128 -2.8; 141 -3.2; 155 -3.6; 170 -3.4; 187 -3.4; 206 -3.0; 227 -2.1; 249 -2.3; 274 -3.2; 302 -3.1; 332 -2.4; 365 -1.2; 402 0.1; 442 1.7; 486 2.9; 535 3.4; 588 4.2; 647 4.2; 712 3.1; 783 2.2; 861 1.2; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -0.9; 1387 -2.2; 1526 -2.7; 1678 -3.1; 1846 -3.2; 2031 -3.2; 2234 -3.8; 2457 -2.2; 2703 -0.4; 2973 1.5; 3270 2.8; 3597 5.1; 3957 5.5; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.7; 6373 1.1; 7010 1.4; 7711 0.3; 8482 -0.9; 9330 -1.9; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.2; 18182 -3.5; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 226 Hz   |  0.73 | -3.9 dB |
| Peaking | 589 Hz   |  1.57 | 5.8 dB  |
| Peaking | 1997 Hz  |  1.23 | -4.9 dB |
| Peaking | 4292 Hz  |  1.51 | 7.7 dB  |
| Peaking | 18633 Hz |  1.25 | -3.8 dB |
| Peaking | 27 Hz    |  0.91 | 2.4 dB  |
| Peaking | 76 Hz    |  5.76 | 1.2 dB  |
| Peaking | 1427 Hz  |  3.01 | -0.1 dB |
| Peaking | 5610 Hz  | 10.98 | 2.7 dB  |
| Peaking | 8903 Hz  |  4.55 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20320/Phiaton%20PS%20320.png)