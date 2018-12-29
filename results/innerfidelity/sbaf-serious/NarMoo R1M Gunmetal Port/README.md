# NarMoo R1M Gunmetal Port
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -10.2; 23 -9.9; 25 -9.7; 28 -9.4; 31 -9.1; 34 -8.8; 37 -8.6; 41 -8.4; 45 -8.2; 49 -8.0; 54 -7.9; 60 -7.8; 66 -7.8; 72 -7.8; 79 -7.8; 87 -7.9; 96 -8.1; 106 -8.0; 116 -7.9; 128 -8.0; 141 -7.9; 155 -7.8; 170 -7.7; 187 -7.5; 206 -7.3; 227 -6.9; 249 -6.6; 274 -6.2; 302 -5.8; 332 -5.3; 365 -4.8; 402 -4.3; 442 -3.6; 486 -3.3; 535 -2.6; 588 -1.8; 647 -1.3; 712 -0.9; 783 -0.4; 861 -0.5; 947 -0.1; 1042 0.0; 1146 0.0; 1261 0.0; 1387 -0.3; 1526 -0.7; 1678 -0.8; 1846 -0.8; 2031 -0.5; 2234 -0.4; 2457 0.1; 2703 -0.3; 2973 -0.6; 3270 -0.7; 3597 -1.2; 3957 -2.3; 4353 -5.2; 4788 -7.6; 5267 -7.1; 5793 -2.9; 6373 1.1; 7010 2.2; 7711 0.3; 8482 0.0; 9330 -0.5; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.5; 18182 -3.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo R1M Gunmetal Port GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Gunmetal Port ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 11 Hz    |  0.12 | -9.5 dB |
| Peaking | 199 Hz   |  0.59 | -5.8 dB |
| Peaking | 5045 Hz  |  3.01 | -9.6 dB |
| Peaking | 6580 Hz  |  2.7  | 4.0 dB  |
| Peaking | 17860 Hz |  3.31 | -3.8 dB |
| Peaking | 13 Hz    |  0.75 | -1.0 dB |
| Peaking | 44 Hz    |  1.7  | 0.6 dB  |
| Peaking | 437 Hz   |  2.1  | -0.7 dB |
| Peaking | 850 Hz   |  1.46 | 0.9 dB  |
| Peaking | 4428 Hz  | 13.69 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Gunmetal%20Port/NarMoo%20R1M%20Gunmetal%20Port.png)