# Audeze Sine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.9; 37 5.9; 41 5.8; 45 5.5; 49 5.3; 54 5.0; 60 4.6; 66 4.1; 72 3.8; 79 3.7; 87 3.3; 96 2.6; 106 2.2; 116 1.9; 128 1.5; 141 1.4; 155 1.1; 170 1.1; 187 1.2; 206 1.4; 227 1.0; 249 0.7; 274 0.5; 302 0.4; 332 0.4; 365 0.4; 402 0.4; 442 0.1; 486 -0.1; 535 -0.0; 588 0.0; 647 0.3; 712 0.4; 783 0.4; 861 0.4; 947 0.1; 1042 -0.0; 1146 -0.5; 1261 -0.9; 1387 -1.3; 1526 -1.1; 1678 -1.0; 1846 -1.4; 2031 -1.8; 2234 -2.1; 2457 -1.7; 2703 -2.4; 2973 -2.8; 3270 -3.0; 3597 -2.8; 3957 -0.7; 4353 1.9; 4788 3.1; 5267 3.2; 5793 3.9; 6373 4.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -2.2; 11289 -5.2; 12418 -4.6; 13660 -3.4; 15026 -3.5; 16529 -5.8; 18182 -7.7; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.37 | 6.1 dB  |
| Peaking | 3467 Hz  |  1.04 | -6.3 dB |
| Peaking | 5169 Hz  |  1.13 | 7.6 dB  |
| Peaking | 11519 Hz |  3.22 | -4.6 dB |
| Peaking | 18896 Hz |  0.82 | -8.1 dB |
| Peaking | 529 Hz   |  2.27 | -0.7 dB |
| Peaking | 732 Hz   |  0.79 | 0.8 dB  |
| Peaking | 1351 Hz  |  2.65 | -0.9 dB |
| Peaking | 6607 Hz  | 10.94 | 2.1 dB  |
| Peaking | 7630 Hz  |  5.84 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Audeze%20Sine/Audeze%20Sine.png)