# Bose QuietComfort 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.8; 25 0.7; 28 -0.3; 31 -0.8; 34 -0.9; 37 -0.9; 41 -0.7; 45 -0.5; 49 -0.3; 54 -0.2; 60 -0.3; 66 -0.5; 72 -0.9; 79 -1.4; 87 -2.0; 96 -2.5; 106 -2.9; 116 -2.9; 128 -2.9; 141 -2.9; 155 -2.8; 170 -2.8; 187 -2.8; 206 -2.9; 227 -2.7; 249 -2.6; 274 -2.4; 302 -2.3; 332 -2.2; 365 -2.2; 402 -2.2; 442 -2.2; 486 -2.1; 535 -1.8; 588 -1.2; 647 -1.1; 712 -1.2; 783 -0.6; 861 -0.0; 947 0.1; 1042 -0.3; 1146 -1.1; 1261 -2.2; 1387 -3.7; 1526 -5.4; 1678 -6.0; 1846 -4.8; 2031 -3.5; 2234 -2.6; 2457 -1.6; 2703 -0.9; 2973 0.9; 3270 2.3; 3597 1.8; 3957 -0.7; 4353 -2.6; 4788 0.9; 5267 5.7; 5793 6.0; 6373 5.5; 7010 -0.5; 7711 -2.4; 8482 -0.1; 9330 -0.1; 10263 -0.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 155 Hz  |  0.7  | -3.1 dB |
| Peaking | 425 Hz  |  1.75 | -1.4 dB |
| Peaking | 1691 Hz |  2.34 | -6.1 dB |
| Peaking | 3304 Hz |  7.61 | 3.2 dB  |
| Peaking | 5762 Hz |  5.14 | 7.3 dB  |
| Peaking | 58 Hz   |  3.82 | 0.7 dB  |
| Peaking | 962 Hz  |  4.84 | 1.3 dB  |
| Peaking | 4309 Hz | 10.42 | -3.7 dB |
| Peaking | 6524 Hz |  7.07 | 3.7 dB  |
| Peaking | 7364 Hz |  5.51 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)