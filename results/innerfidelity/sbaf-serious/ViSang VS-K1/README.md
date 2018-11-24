# ViSang VS-K1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.1; 28 2.6; 31 2.2; 34 1.9; 37 1.6; 41 1.2; 45 0.9; 49 0.7; 54 0.3; 60 0.0; 66 -0.3; 72 -0.6; 79 -1.0; 87 -1.4; 96 -1.7; 106 -1.9; 116 -2.0; 128 -2.2; 141 -2.3; 155 -2.3; 170 -2.2; 187 -2.1; 206 -2.0; 227 -1.7; 249 -1.5; 274 -1.2; 302 -0.9; 332 -0.6; 365 -0.3; 402 -0.0; 442 0.4; 486 0.5; 535 0.8; 588 1.2; 647 1.2; 712 1.2; 783 1.2; 861 0.8; 947 0.3; 1042 -0.3; 1146 -0.5; 1261 -0.8; 1387 -1.9; 1526 -0.7; 1678 -1.7; 1846 -2.5; 2031 -1.4; 2234 0.4; 2457 3.3; 2703 5.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ViSang VS-K1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ViSang VS-K1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.52 | 4.7 dB  |
| Peaking | 142 Hz  | 0.65 | -2.6 dB |
| Peaking | 622 Hz  | 1.59 | 1.5 dB  |
| Peaking | 1836 Hz | 1.6  | -5.7 dB |
| Peaking | 3507 Hz | 0.81 | 7.8 dB  |
| Peaking | 1109 Hz | 6.69 | -0.6 dB |
| Peaking | 2737 Hz | 7.01 | 1.7 dB  |
| Peaking | 3683 Hz | 2.77 | -1.1 dB |
| Peaking | 6194 Hz | 2.24 | 5.6 dB  |
| Peaking | 7428 Hz | 1.47 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ViSang%20VS-K1/ViSang%20VS-K1.png)