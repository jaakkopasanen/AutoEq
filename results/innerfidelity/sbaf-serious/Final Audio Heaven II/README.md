# Final Audio Heaven II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 5.1; 25 4.9; 28 4.8; 31 4.6; 34 4.4; 37 4.3; 41 4.1; 45 3.9; 49 3.7; 54 3.4; 60 3.1; 66 2.8; 72 2.4; 79 2.0; 87 1.5; 96 1.1; 106 0.8; 116 0.5; 128 0.2; 141 -0.2; 155 -0.4; 170 -0.6; 187 -0.7; 206 -0.9; 227 -0.8; 249 -0.9; 274 -0.8; 302 -0.8; 332 -0.8; 365 -0.6; 402 -0.5; 442 -0.2; 486 -0.2; 535 0.1; 588 0.5; 647 0.6; 712 0.6; 783 0.8; 861 0.6; 947 0.3; 1042 -0.0; 1146 -0.4; 1261 -0.9; 1387 -1.5; 1526 -2.1; 1678 -2.6; 1846 -2.7; 2031 -2.9; 2234 -3.2; 2457 -3.2; 2703 -2.8; 2973 -0.4; 3270 2.9; 3597 5.2; 3957 5.9; 4353 4.8; 4788 4.6; 5267 5.2; 5793 4.7; 6373 2.2; 7010 0.9; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.93 | 5.1 dB  |
| Peaking | 54 Hz   | 1.54 | 2.4 dB  |
| Peaking | 2493 Hz | 1.26 | -5.2 dB |
| Peaking | 3707 Hz | 2.32 | 7.8 dB  |
| Peaking | 5413 Hz | 3.32 | 4.6 dB  |
| Peaking | 252 Hz  | 0.99 | -1.1 dB |
| Peaking | 772 Hz  | 1.44 | 1.2 dB  |
| Peaking | 1539 Hz | 3.98 | -0.9 dB |
| Peaking | 8385 Hz | 3.16 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Heaven%20II/Final%20Audio%20Heaven%20II.png)