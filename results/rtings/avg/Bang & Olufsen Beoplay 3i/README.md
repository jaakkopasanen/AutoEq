# Bang & Olufsen Beoplay Earset 3i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 4.9; 72 3.9; 79 2.9; 87 2.0; 96 1.1; 106 0.5; 116 -0.0; 128 -0.4; 141 -0.6; 155 -0.7; 170 -0.8; 187 -0.8; 206 -0.9; 227 -1.0; 249 -1.0; 274 -1.2; 302 -1.3; 332 -1.3; 365 -1.4; 402 0.2; 442 -0.1; 486 -0.1; 535 -0.2; 588 0.1; 647 0.3; 712 -0.0; 783 -0.1; 861 -0.0; 947 0.0; 1042 0.0; 1146 -0.0; 1261 -0.2; 1387 -0.3; 1526 -0.4; 1678 -0.4; 1846 -0.1; 2031 1.0; 2234 3.0; 2457 5.1; 2703 6.0; 2973 5.7; 3270 4.5; 3597 3.1; 3957 1.8; 4353 0.4; 4788 -0.5; 5267 -1.7; 5793 -1.6; 6373 0.3; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay Earset 3i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay Earset 3i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.37 | 8.8 dB  |
| Peaking | 119 Hz  | 0.52 | -5.6 dB |
| Peaking | 2852 Hz | 2.48 | 6.6 dB  |
| Peaking | 5449 Hz | 3.39 | -2.7 dB |
| Peaking | 6764 Hz | 6.52 | 2.6 dB  |
| Peaking | 38 Hz   | 2.92 | -0.5 dB |
| Peaking | 608 Hz  | 1.85 | 0.5 dB  |
| Peaking | 2257 Hz | 1.29 | -2.4 dB |
| Peaking | 2372 Hz | 3.84 | 3.3 dB  |
| Peaking | 3616 Hz | 3.62 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%203i/Bang%20&%20Olufsen%20Beoplay%20Earset%203i.png)