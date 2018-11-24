# Alpha Design Labs H128

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.3; 25 -0.8; 28 -1.4; 31 -1.9; 34 -2.3; 37 -2.6; 41 -3.0; 45 -3.2; 49 -3.4; 54 -3.6; 60 -3.8; 66 -4.0; 72 -4.2; 79 -4.5; 87 -4.7; 96 -4.9; 106 -4.7; 116 -4.5; 128 -4.4; 141 -5.0; 155 -5.2; 170 -4.6; 187 -4.4; 206 -4.2; 227 -4.0; 249 -3.7; 274 -3.2; 302 -3.0; 332 -2.6; 365 -2.3; 402 -2.0; 442 -2.0; 486 -2.0; 535 -2.0; 588 -1.7; 647 -1.6; 712 -1.7; 783 -1.4; 861 -1.0; 947 -0.0; 1042 -0.3; 1146 -0.7; 1261 -0.3; 1387 -0.2; 1526 -0.1; 1678 -0.0; 1846 0.4; 2031 0.9; 2234 0.6; 2457 1.5; 2703 2.4; 2973 3.3; 3270 4.0; 3597 5.6; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.6; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Alpha Design Labs H128 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha Design Labs H128 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.41 | 2.1 dB  |
| Peaking | 64 Hz   | 0.46 | -3.4 dB |
| Peaking | 175 Hz  | 0.72 | -3.0 dB |
| Peaking | 609 Hz  | 0.69 | -1.1 dB |
| Peaking | 4524 Hz | 1.28 | 6.9 dB  |
| Peaking | 12 Hz   | 1    | 0.8 dB  |
| Peaking | 3695 Hz | 3.36 | 1.4 dB  |
| Peaking | 4367 Hz | 2.95 | -1.4 dB |
| Peaking | 6311 Hz | 3.13 | 4.4 dB  |
| Peaking | 7501 Hz | 1.5  | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20Design%20Labs%20H128/Alpha%20Design%20Labs%20H128.png)