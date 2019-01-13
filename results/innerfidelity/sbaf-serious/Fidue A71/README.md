# Fidue A71
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.7; 23 -2.1; 25 -2.5; 28 -2.9; 31 -3.2; 34 -3.5; 37 -3.7; 41 -4.0; 45 -4.2; 49 -4.5; 54 -4.8; 60 -5.1; 66 -5.4; 72 -5.7; 79 -6.0; 87 -6.3; 96 -6.7; 106 -6.8; 116 -6.9; 128 -7.1; 141 -7.1; 155 -7.1; 170 -7.0; 187 -6.7; 206 -6.5; 227 -6.1; 249 -5.8; 274 -5.3; 302 -4.8; 332 -4.3; 365 -3.8; 402 -3.4; 442 -2.3; 486 -1.6; 535 -1.2; 588 -0.4; 647 0.1; 712 0.2; 783 0.7; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.5; 1387 -2.7; 1526 -4.1; 1678 -5.1; 1846 -5.0; 2031 -3.8; 2234 -2.1; 2457 -0.0; 2703 2.6; 2973 5.6; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 2.0; 7010 -2.0; 7711 -1.3; 8482 -0.9; 9330 -0.8; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A71 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A71 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 88 Hz    | 0.38 | -5.3 dB  |
| Peaking | 222 Hz   | 0.7  | -3.5 dB  |
| Peaking | 1882 Hz  | 1.17 | -14.9 dB |
| Peaking | 3136 Hz  | 0.39 | 12.0 dB  |
| Peaking | 7972 Hz  | 1.32 | -7.2 dB  |
| Peaking | 2446 Hz  | 8.07 | -1.3 dB  |
| Peaking | 4619 Hz  | 2.07 | -3.3 dB  |
| Peaking | 5966 Hz  | 1.29 | 5.4 dB   |
| Peaking | 6901 Hz  | 4.83 | -6.1 dB  |
| Peaking | 13016 Hz | 0.83 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A71/Fidue%20A71.png)