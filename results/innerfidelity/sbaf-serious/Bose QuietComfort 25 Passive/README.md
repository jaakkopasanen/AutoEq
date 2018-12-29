# Bose QuietComfort 25 Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.3; 25 0.6; 28 -0.3; 31 -1.1; 34 -1.8; 37 -2.5; 41 -3.3; 45 -4.0; 49 -4.6; 54 -5.2; 60 -5.8; 66 -6.2; 72 -6.4; 79 -6.5; 87 -6.3; 96 -6.1; 106 -6.1; 116 -6.2; 128 -5.4; 141 -5.4; 155 -6.7; 170 -3.8; 187 -4.8; 206 -4.6; 227 -3.2; 249 -2.3; 274 -1.2; 302 -0.0; 332 0.8; 365 1.4; 402 1.7; 442 1.9; 486 1.7; 535 1.4; 588 1.3; 647 0.8; 712 0.1; 783 -0.3; 861 -0.8; 947 -0.6; 1042 0.5; 1146 1.9; 1261 3.6; 1387 5.3; 1526 5.8; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 5.0; 3597 4.9; 3957 5.0; 4353 5.6; 4788 6.0; 5267 6.0; 5793 5.8; 6373 4.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.97 | 3.1 dB  |
| Peaking | 73 Hz   | 0.83 | -6.4 dB |
| Peaking | 160 Hz  | 1.7  | -3.7 dB |
| Peaking | 2128 Hz | 0.94 | 6.4 dB  |
| Peaking | 5129 Hz | 1.99 | 5.1 dB  |
| Peaking | 223 Hz  | 3.38 | -1.7 dB |
| Peaking | 421 Hz  | 1.21 | 2.3 dB  |
| Peaking | 902 Hz  | 2.07 | -2.9 dB |
| Peaking | 1416 Hz | 4.37 | 2.1 dB  |
| Peaking | 8510 Hz | 3.79 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2025%20Passive/Bose%20QuietComfort%2025%20Passive.png)