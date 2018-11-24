# I-Mego Throne

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.3; 23 -3.4; 25 -3.5; 28 -3.6; 31 -3.6; 34 -3.6; 37 -3.6; 41 -3.7; 45 -3.9; 49 -4.0; 54 -4.2; 60 -4.4; 66 -4.5; 72 -4.7; 79 -4.8; 87 -5.1; 96 -5.3; 106 -5.2; 116 -5.3; 128 -5.5; 141 -5.8; 155 -5.6; 170 -5.1; 187 -4.8; 206 -4.3; 227 -3.5; 249 -2.8; 274 -1.9; 302 -1.1; 332 -0.7; 365 -1.5; 402 -1.7; 442 -2.4; 486 -3.3; 535 -3.5; 588 -3.2; 647 -2.9; 712 -2.4; 783 -1.5; 861 -0.9; 947 -0.2; 1042 0.3; 1146 0.7; 1261 1.5; 1387 1.9; 1526 2.3; 1678 3.0; 1846 4.1; 2031 5.7; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`I-Mego Throne GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `I-Mego Throne ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.4  | -3.2 dB |
| Peaking | 98 Hz   | 0.97 | -3.0 dB |
| Peaking | 168 Hz  | 1.58 | -3.5 dB |
| Peaking | 603 Hz  | 1.47 | -3.7 dB |
| Peaking | 3282 Hz | 0.66 | 6.9 dB  |
| Peaking | 218 Hz  | 5.25 | -0.3 dB |
| Peaking | 2164 Hz | 3.07 | 2.2 dB  |
| Peaking | 2693 Hz | 0.88 | -1.2 dB |
| Peaking | 6172 Hz | 2    | 5.6 dB  |
| Peaking | 7537 Hz | 1.46 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/I-Mego%20Throne/I-Mego%20Throne.png)