# Focal Spirit One Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.6; 23 -3.6; 25 -3.6; 28 -3.6; 31 -3.5; 34 -3.4; 37 -3.4; 41 -3.3; 45 -3.2; 49 -3.1; 54 -3.0; 60 -2.9; 66 -2.8; 72 -2.7; 79 -2.7; 87 -3.1; 96 -4.3; 106 -4.7; 116 -4.2; 128 -3.9; 141 -4.5; 155 -4.5; 170 -4.2; 187 -4.4; 206 -4.2; 227 -3.9; 249 -3.6; 274 -3.2; 302 -2.8; 332 -2.2; 365 -1.9; 402 -1.4; 442 -1.5; 486 -1.7; 535 -1.4; 588 -0.8; 647 -0.3; 712 0.4; 783 0.4; 861 0.1; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.6; 1387 0.4; 1526 0.1; 1678 0.1; 1846 0.1; 2031 0.4; 2234 0.6; 2457 1.1; 2703 1.2; 2973 0.5; 3270 -0.3; 3597 -0.4; 3957 0.8; 4353 2.1; 4788 2.9; 5267 5.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.4; 10263 -1.5; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  0.71 | -3.3 dB |
| Peaking | 49 Hz   |  1.08 | -1.4 dB |
| Peaking | 103 Hz  |  3.3  | -2.0 dB |
| Peaking | 187 Hz  |  0.82 | -4.2 dB |
| Peaking | 5743 Hz |  3.06 | 6.7 dB  |
| Peaking | 1131 Hz |  1.66 | 0.6 dB  |
| Peaking | 2582 Hz |  4.54 | 1.2 dB  |
| Peaking | 3452 Hz |  6.39 | -1.3 dB |
| Peaking | 6547 Hz | 10.45 | 1.5 dB  |
| Peaking | 9741 Hz |  2.61 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%20Classic/Focal%20Spirit%20One%20Classic.png)