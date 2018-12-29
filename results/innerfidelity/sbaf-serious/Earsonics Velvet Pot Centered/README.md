# Earsonics Velvet Pot Centered
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.3; 23 -1.5; 25 -1.7; 28 -2.0; 31 -2.1; 34 -2.3; 37 -2.4; 41 -2.4; 45 -2.5; 49 -2.5; 54 -2.5; 60 -2.5; 66 -2.5; 72 -2.5; 79 -2.4; 87 -2.2; 96 -2.0; 106 -1.5; 116 -0.9; 128 -0.3; 141 0.6; 155 1.5; 170 2.6; 187 3.8; 206 4.8; 227 5.6; 249 5.8; 274 5.6; 302 4.9; 332 4.3; 365 3.5; 402 2.9; 442 2.5; 486 1.9; 535 1.5; 588 1.6; 647 1.4; 712 1.1; 783 1.1; 861 0.7; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.4; 1526 -1.7; 1678 -1.6; 1846 -0.6; 2031 1.5; 2234 3.2; 2457 4.6; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 1.9; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot Centered GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot Centered ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.67 | -1.6 dB |
| Peaking | 103 Hz  | 0.61 | -3.0 dB |
| Peaking | 239 Hz  | 0.94 | 7.1 dB  |
| Peaking | 1579 Hz | 1.82 | -4.6 dB |
| Peaking | 3512 Hz | 0.78 | 7.2 dB  |
| Peaking | 1872 Hz | 8.89 | -0.6 dB |
| Peaking | 2657 Hz | 3.13 | 1.2 dB  |
| Peaking | 3433 Hz | 2.56 | -1.1 dB |
| Peaking | 6129 Hz | 2.56 | 5.3 dB  |
| Peaking | 7300 Hz | 1.42 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20Centered/Earsonics%20Velvet%20Pot%20Centered.png)