# PSB M4U 8 Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 21 -5.5; 23 -5.5; 25 -5.5; 28 -5.4; 31 -5.3; 34 -5.2; 37 -5.1; 41 -4.9; 45 -4.7; 49 -4.5; 54 -4.6; 60 -4.9; 66 -5.0; 72 -4.8; 79 -4.5; 87 -4.3; 96 -4.4; 106 -5.5; 116 -5.9; 128 -6.5; 141 -7.0; 155 -6.3; 170 -5.3; 187 -6.2; 206 -5.4; 227 -4.6; 249 -3.8; 274 -3.0; 302 -2.9; 332 -2.2; 365 -1.3; 402 -0.5; 442 0.3; 486 0.5; 535 1.1; 588 1.7; 647 1.9; 712 1.6; 783 1.2; 861 0.4; 947 0.1; 1042 -0.1; 1146 -0.6; 1261 -1.1; 1387 -1.2; 1526 -1.4; 1678 -1.4; 1846 -1.0; 2031 -0.2; 2234 -0.5; 2457 -0.4; 2703 -0.5; 2973 -0.8; 3270 -1.4; 3597 -2.1; 3957 -2.7; 4353 -2.3; 4788 -0.9; 5267 -0.5; 5793 0.2; 6373 0.2; 7010 -0.2; 7711 0.1; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 8 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 8 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 1.02 | -5.1 dB |
| Peaking | 32 Hz   | 0.48 | -4.2 dB |
| Peaking | 157 Hz  | 0.81 | -5.9 dB |
| Peaking | 597 Hz  | 2.1  | 2.7 dB  |
| Peaking | 3906 Hz | 2.68 | -2.7 dB |
| Peaking | 761 Hz  | 5.18 | 0.7 dB  |
| Peaking | 1575 Hz | 1.84 | -1.9 dB |
| Peaking | 1920 Hz | 1.65 | 0.7 dB  |
| Peaking | 6114 Hz | 4.97 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%208%20Wired%20Passive/PSB%20M4U%208%20Wired%20Passive.png)