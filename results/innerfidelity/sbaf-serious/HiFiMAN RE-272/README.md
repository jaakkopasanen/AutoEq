# HiFiMAN RE-272
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.0; 25 4.9; 28 4.8; 31 4.7; 34 4.7; 37 4.6; 41 4.5; 45 4.2; 49 4.0; 54 3.8; 60 3.5; 66 3.2; 72 2.9; 79 2.5; 87 2.0; 96 1.5; 106 1.2; 116 1.0; 128 0.6; 141 0.2; 155 -0.0; 170 -0.2; 187 -0.4; 206 -0.6; 227 -0.7; 249 -0.8; 274 -0.8; 302 -0.8; 332 -0.8; 365 -0.9; 402 -0.8; 442 -0.5; 486 -0.5; 535 -0.2; 588 0.5; 647 0.9; 712 1.2; 783 1.5; 861 1.2; 947 0.6; 1042 -0.4; 1146 -1.4; 1261 -2.7; 1387 -4.4; 1526 -6.3; 1678 -7.9; 1846 -8.6; 2031 -7.3; 2234 -4.5; 2457 -0.6; 2703 3.1; 2973 5.8; 3270 6.0; 3597 6.0; 3957 4.5; 4353 2.1; 4788 2.9; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -2.0; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-272 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-272 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.81 | 4.9 dB   |
| Peaking | 59 Hz   | 1.42 | 2.3 dB   |
| Peaking | 1853 Hz | 2.17 | -10.6 dB |
| Peaking | 3166 Hz | 2.13 | 8.1 dB   |
| Peaking | 5807 Hz | 3.55 | 6.2 dB   |
| Peaking | 100 Hz  | 1.45 | 0.6 dB   |
| Peaking | 325 Hz  | 0.52 | -1.2 dB  |
| Peaking | 785 Hz  | 1.55 | 2.6 dB   |
| Peaking | 1415 Hz | 4.26 | -1.4 dB  |
| Peaking | 9273 Hz | 6.16 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-272/HiFiMAN%20RE-272.png)