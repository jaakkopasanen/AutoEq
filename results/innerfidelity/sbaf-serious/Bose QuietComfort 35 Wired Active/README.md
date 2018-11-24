# Bose QuietComfort 35 Wired Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -1.4; 23 -1.3; 25 -1.2; 28 -1.3; 31 -1.6; 34 -1.8; 37 -2.0; 41 -2.2; 45 -2.3; 49 -2.2; 54 -2.1; 60 -2.0; 66 -1.8; 72 -1.7; 79 -1.8; 87 -1.9; 96 -2.0; 106 -2.0; 116 -1.8; 128 -1.7; 141 -1.6; 155 -1.5; 170 -1.2; 187 -1.2; 206 -1.2; 227 -0.9; 249 -0.8; 274 -0.5; 302 -0.2; 332 -0.0; 365 0.2; 402 0.4; 442 0.6; 486 0.5; 535 0.5; 588 0.8; 647 0.7; 712 0.5; 783 0.5; 861 0.1; 947 -0.0; 1042 0.1; 1146 0.6; 1261 0.8; 1387 -0.1; 1526 0.5; 1678 -0.7; 1846 -1.6; 2031 -2.0; 2234 -2.0; 2457 -2.3; 2703 -2.6; 2973 -2.2; 3270 -0.9; 3597 -1.4; 3957 -2.1; 4353 -1.7; 4788 0.4; 5267 5.5; 5793 0.5; 6373 0.3; 7010 1.7; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 Wired Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  0.66 | -2.0 dB |
| Peaking | 127 Hz  |  1.17 | -1.3 dB |
| Peaking | 2510 Hz |  2.3  | -2.7 dB |
| Peaking | 4136 Hz |  4.35 | -2.2 dB |
| Peaking | 5300 Hz |  8.74 | 6.6 dB  |
| Peaking | 225 Hz  |  2.49 | -0.5 dB |
| Peaking | 516 Hz  |  1.28 | 0.8 dB  |
| Peaking | 1340 Hz |  2.37 | 0.8 dB  |
| Peaking | 1898 Hz |  5.99 | -1.2 dB |
| Peaking | 6979 Hz | 11.76 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wired%20Active/Bose%20QuietComfort%2035%20Wired%20Active.png)