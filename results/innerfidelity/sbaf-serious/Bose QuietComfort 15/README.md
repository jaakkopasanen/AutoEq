# Bose QuietComfort 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.5; 23 -1.9; 25 -2.3; 28 -2.7; 31 -3.0; 34 -3.1; 37 -3.2; 41 -3.3; 45 -3.4; 49 -3.3; 54 -3.3; 60 -3.3; 66 -3.3; 72 -3.3; 79 -3.6; 87 -3.9; 96 -4.2; 106 -4.2; 116 -4.1; 128 -4.2; 141 -4.1; 155 -3.9; 170 -3.4; 187 -3.4; 206 -3.2; 227 -3.0; 249 -2.8; 274 -2.5; 302 -2.1; 332 -1.7; 365 -1.2; 402 -0.8; 442 -0.4; 486 -0.2; 535 0.1; 588 0.6; 647 0.9; 712 1.0; 783 1.2; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.8; 1261 -1.3; 1387 -1.4; 1526 -1.8; 1678 -2.6; 1846 -3.0; 2031 -2.6; 2234 -2.0; 2457 -1.7; 2703 -0.3; 2973 1.2; 3270 3.1; 3597 6.0; 3957 -1.1; 4353 -5.3; 4788 -2.6; 5267 1.6; 5793 -3.0; 6373 -3.7; 7010 0.0; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.43 | -2.9 dB |
| Peaking | 153 Hz  | 0.84 | -3.0 dB |
| Peaking | 1914 Hz | 2.1  | -3.2 dB |
| Peaking | 3613 Hz | 4.43 | 10.1 dB |
| Peaking | 4192 Hz | 4.12 | -8.7 dB |
| Peaking | 281 Hz  | 3.04 | -0.7 dB |
| Peaking | 709 Hz  | 2.22 | 1.7 dB  |
| Peaking | 5374 Hz | 7.74 | 5.1 dB  |
| Peaking | 6108 Hz | 4.01 | -5.4 dB |
| Peaking | 7249 Hz | 5.44 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2015/Bose%20QuietComfort%2015.png)