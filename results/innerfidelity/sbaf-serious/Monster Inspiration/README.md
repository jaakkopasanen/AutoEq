# Monster Inspiration
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.1; 23 -0.4; 25 -0.7; 28 -1.0; 31 -1.3; 34 -1.5; 37 -1.7; 41 -2.0; 45 -2.2; 49 -2.4; 54 -2.6; 60 -2.8; 66 -3.0; 72 -3.2; 79 -3.4; 87 -3.7; 96 -3.8; 106 -4.3; 116 -4.5; 128 -4.4; 141 -4.8; 155 -4.8; 170 -4.0; 187 -3.9; 206 -3.2; 227 -2.1; 249 -1.0; 274 0.3; 302 1.9; 332 2.6; 365 3.6; 402 3.8; 442 4.0; 486 3.9; 535 4.2; 588 4.2; 647 3.6; 712 2.5; 783 1.5; 861 0.4; 947 0.1; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.5; 1526 -1.9; 1678 -2.0; 1846 -1.8; 2031 -1.4; 2234 -1.5; 2457 -1.3; 2703 -0.9; 2973 -0.8; 3270 -1.3; 3597 -1.5; 3957 -1.1; 4353 -0.4; 4788 -0.2; 5267 4.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 81 Hz   | 0.52 | -2.6 dB |
| Peaking | 172 Hz  | 0.95 | -4.4 dB |
| Peaking | 462 Hz  | 0.75 | 7.1 dB  |
| Peaking | 1489 Hz | 0.28 | -2.6 dB |
| Peaking | 5926 Hz | 3.3  | 7.9 dB  |
| Peaking | 473 Hz  | 6.63 | -0.8 dB |
| Peaking | 611 Hz  | 4.79 | 0.8 dB  |
| Peaking | 1668 Hz | 1.35 | -0.9 dB |
| Peaking | 2890 Hz | 1.05 | 1.5 dB  |
| Peaking | 3853 Hz | 1.85 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Inspiration/Monster%20Inspiration.png)