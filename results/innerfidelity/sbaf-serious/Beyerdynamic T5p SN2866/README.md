# Beyerdynamic T5p sn2866
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.7; 25 1.4; 28 1.2; 31 1.0; 34 0.8; 37 0.7; 41 0.6; 45 0.6; 49 0.6; 54 0.7; 60 0.8; 66 0.9; 72 1.1; 79 1.4; 87 1.2; 96 -0.0; 106 -1.9; 116 -3.0; 128 -4.0; 141 -4.1; 155 -3.4; 170 -2.1; 187 -3.2; 206 -2.9; 227 -2.3; 249 -1.7; 274 -1.0; 302 -0.5; 332 -0.1; 365 0.1; 402 0.2; 442 0.3; 486 -0.1; 535 -0.4; 588 0.8; 647 3.8; 712 1.3; 783 1.3; 861 -0.3; 947 -0.5; 1042 0.3; 1146 -1.2; 1261 -2.9; 1387 -1.7; 1526 -3.4; 1678 -3.9; 1846 -3.7; 2031 -3.0; 2234 -3.9; 2457 -1.3; 2703 0.6; 2973 1.2; 3270 2.2; 3597 3.4; 3957 5.2; 4353 1.6; 4788 6.0; 5267 5.0; 5793 0.6; 6373 0.2; 7010 2.2; 7711 -1.9; 8482 -5.1; 9330 -2.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p sn2866 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sn2866 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 133 Hz  |  3.67 | -4.3 dB |
| Peaking | 203 Hz  |  3.14 | -2.9 dB |
| Peaking | 1895 Hz |  1.7  | -5.0 dB |
| Peaking | 4281 Hz |  1.27 | 5.1 dB  |
| Peaking | 8478 Hz |  5.31 | -6.4 dB |
| Peaking | 13 Hz   |  0.51 | 2.5 dB  |
| Peaking | 78 Hz   |  3.89 | 1.9 dB  |
| Peaking | 649 Hz  |  5.58 | 4.0 dB  |
| Peaking | 669 Hz  |  0.05 | -0.2 dB |
| Peaking | 5017 Hz | 13.36 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sn2866/Beyerdynamic%20T5p%20sn2866.png)