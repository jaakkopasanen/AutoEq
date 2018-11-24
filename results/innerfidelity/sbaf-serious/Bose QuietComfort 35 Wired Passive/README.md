# Bose QuietComfort 35 Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.5; 28 3.5; 31 2.7; 34 2.0; 37 1.5; 41 0.9; 45 0.4; 49 0.1; 54 -0.2; 60 -0.3; 66 -0.3; 72 -0.4; 79 -0.2; 87 -0.3; 96 -0.7; 106 -2.0; 116 -2.9; 128 -4.3; 141 -5.2; 155 -4.1; 170 -2.0; 187 -3.4; 206 -2.6; 227 -1.1; 249 0.2; 274 1.5; 302 2.2; 332 2.6; 365 2.6; 402 2.4; 442 2.1; 486 1.4; 535 0.7; 588 0.3; 647 -0.6; 712 -1.5; 783 -1.8; 861 -1.8; 947 -0.8; 1042 0.8; 1146 2.4; 1261 3.7; 1387 4.6; 1526 5.4; 1678 5.3; 1846 5.1; 2031 5.6; 2234 5.9; 2457 5.3; 2703 4.7; 2973 3.8; 3270 1.7; 3597 -0.9; 3957 -0.2; 4353 1.0; 4788 3.4; 5267 6.0; 5793 2.5; 6373 4.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-70**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.42 | 6.6 dB  |
| Peaking | 145 Hz  |  1.65 | -4.9 dB |
| Peaking | 343 Hz  |  2.45 | 3.5 dB  |
| Peaking | 1956 Hz |  1.47 | 6.3 dB  |
| Peaking | 5453 Hz |  3.63 | 5.1 dB  |
| Peaking | 827 Hz  |  2.96 | -3.1 dB |
| Peaking | 1321 Hz |  4.05 | 2.1 dB  |
| Peaking | 2852 Hz |  4.41 | 2.0 dB  |
| Peaking | 3721 Hz |  4.67 | -3.2 dB |
| Peaking | 6632 Hz | 12.23 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wired%20Passive/Bose%20QuietComfort%2035%20Wired%20Passive.png)