# Bose QuietComfort 35 Wireless Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -5.1; 23 -4.4; 25 -3.8; 28 -3.3; 31 -3.0; 34 -3.0; 37 -2.9; 41 -2.9; 45 -2.8; 49 -2.7; 54 -2.5; 60 -2.2; 66 -2.1; 72 -2.0; 79 -2.1; 87 -2.2; 96 -2.3; 106 -2.2; 116 -2.1; 128 -2.0; 141 -1.9; 155 -1.7; 170 -1.2; 187 -1.3; 206 -1.2; 227 -1.0; 249 -0.8; 274 -0.5; 302 -0.2; 332 0.0; 365 0.3; 402 0.5; 442 0.8; 486 0.7; 535 0.8; 588 1.0; 647 0.9; 712 0.5; 783 0.5; 861 0.1; 947 -0.1; 1042 0.2; 1146 1.0; 1261 2.1; 1387 2.3; 1526 3.1; 1678 1.9; 1846 1.6; 2031 -0.1; 2234 -1.2; 2457 -1.5; 2703 -2.7; 2973 -2.1; 3270 -0.2; 3597 -0.1; 3957 -2.4; 4353 -2.2; 4788 -0.4; 5267 4.6; 5793 1.8; 6373 -1.0; 7010 1.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 Wireless Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 10 Hz   |  0.27 | -5.2 dB |
| Peaking | 115 Hz  |  1.03 | -1.7 dB |
| Peaking | 1613 Hz |  1.44 | 4.9 dB  |
| Peaking | 2362 Hz |  0.97 | -3.7 dB |
| Peaking | 5446 Hz | 10.8  | 6.9 dB  |
| Peaking | 541 Hz  |  1.66 | 1.0 dB  |
| Peaking | 974 Hz  |  4.45 | -1.0 dB |
| Peaking | 3502 Hz |  6.79 | 3.8 dB  |
| Peaking | 3856 Hz |  3    | -2.2 dB |
| Peaking | 7194 Hz | 10.87 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wireless%20Active/Bose%20QuietComfort%2035%20Wireless%20Active.png)