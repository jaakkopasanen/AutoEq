# Focal Spirit One 2013 B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.5; 23 -3.4; 25 -3.3; 28 -3.1; 31 -2.9; 34 -2.8; 37 -2.6; 41 -2.4; 45 -2.2; 49 -2.0; 54 -1.9; 60 -1.8; 66 -1.5; 72 -1.0; 79 -0.4; 87 -1.7; 96 -4.3; 106 -4.6; 116 -4.2; 128 -4.0; 141 -4.3; 155 -4.0; 170 -3.9; 187 -3.7; 206 -3.3; 227 -2.8; 249 -2.2; 274 -1.5; 302 -1.4; 332 -1.5; 365 -1.8; 402 -2.4; 442 -2.4; 486 -2.3; 535 -2.1; 588 -1.6; 647 -1.4; 712 -1.2; 783 -0.6; 861 -0.6; 947 -0.3; 1042 0.1; 1146 0.5; 1261 0.7; 1387 0.6; 1526 0.5; 1678 0.5; 1846 0.8; 2031 1.3; 2234 2.0; 2457 2.9; 2703 3.4; 2973 3.3; 3270 2.8; 3597 1.9; 3957 3.5; 4353 0.4; 4788 0.2; 5267 4.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One 2013 B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One 2013 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  0.95 | -3.4 dB |
| Peaking | 141 Hz  |  1.01 | -4.4 dB |
| Peaking | 489 Hz  |  1.67 | -2.1 dB |
| Peaking | 2806 Hz |  1.8  | 3.4 dB  |
| Peaking | 5972 Hz |  4.25 | 6.5 dB  |
| Peaking | 80 Hz   |  5.13 | 2.0 dB  |
| Peaking | 100 Hz  |  5.91 | -2.1 dB |
| Peaking | 1213 Hz |  5.52 | 0.7 dB  |
| Peaking | 3932 Hz | 16.89 | 1.8 dB  |
| Peaking | 9696 Hz |  2.22 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%202013%20B/Focal%20Spirit%20One%202013%20B.png)