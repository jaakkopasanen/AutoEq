# Bowers & Wilkins P3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.4; 25 -0.1; 28 -0.8; 31 -1.4; 34 -2.0; 37 -2.5; 41 -3.0; 45 -3.5; 49 -3.9; 54 -4.4; 60 -4.9; 66 -5.3; 72 -5.8; 79 -6.2; 87 -6.8; 96 -7.3; 106 -7.7; 116 -7.9; 128 -8.2; 141 -8.3; 155 -8.7; 170 -8.8; 187 -8.9; 206 -9.2; 227 -9.3; 249 -9.5; 274 -9.5; 302 -9.4; 332 -9.2; 365 -8.8; 402 -8.2; 442 -7.3; 486 -6.8; 535 -6.2; 588 -5.2; 647 -4.1; 712 -3.0; 783 -1.8; 861 -0.9; 947 -0.3; 1042 0.3; 1146 1.5; 1261 2.3; 1387 1.6; 1526 2.0; 1678 2.3; 1846 3.2; 2031 3.8; 2234 3.8; 2457 4.0; 2703 3.3; 2973 2.0; 3270 0.5; 3597 0.1; 3957 0.6; 4353 3.5; 4788 6.0; 5267 3.2; 5793 2.4; 6373 3.2; 7010 0.9; 7711 -2.0; 8482 -3.5; 9330 -2.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -2.9; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 104 Hz  | 0.55 | -5.4 dB |
| Peaking | 330 Hz  | 0.58 | -8.0 dB |
| Peaking | 1684 Hz | 0.71 | 4.1 dB  |
| Peaking | 4862 Hz | 5.12 | 5.6 dB  |
| Peaking | 8510 Hz | 5.48 | -4.3 dB |
| Peaking | 20 Hz   | 2.08 | 2.3 dB  |
| Peaking | 1626 Hz | 3.02 | -2.1 dB |
| Peaking | 2295 Hz | 1.06 | 1.8 dB  |
| Peaking | 3518 Hz | 3.15 | -2.9 dB |
| Peaking | 6353 Hz | 8.59 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P3/Bowers%20&%20Wilkins%20P3.png)