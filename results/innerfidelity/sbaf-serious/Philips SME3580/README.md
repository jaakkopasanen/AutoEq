# Philips SME3580
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 -12.7; 23 -12.5; 25 -12.3; 28 -12.0; 31 -11.7; 34 -11.4; 37 -11.1; 41 -10.7; 45 -10.4; 49 -10.1; 54 -9.8; 60 -9.5; 66 -9.3; 72 -9.0; 79 -8.9; 87 -8.7; 96 -8.5; 106 -8.1; 116 -7.7; 128 -7.5; 141 -7.1; 155 -6.8; 170 -6.3; 187 -5.9; 206 -5.4; 227 -4.8; 249 -4.3; 274 -3.8; 302 -3.3; 332 -2.7; 365 -2.2; 402 -1.7; 442 -1.1; 486 -0.8; 535 -0.4; 588 0.2; 647 0.5; 712 0.5; 783 0.8; 861 0.7; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.7; 1387 -2.8; 1526 -4.0; 1678 -4.9; 1846 -5.6; 2031 -6.3; 2234 -7.4; 2457 -7.9; 2703 -7.2; 2973 -4.2; 3270 -1.0; 3597 0.6; 3957 -0.2; 4353 -3.3; 4788 -6.7; 5267 -7.8; 5793 -4.5; 6373 -1.0; 7010 1.7; 7711 0.3; 8482 0.0; 9330 -0.7; 10263 -0.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SME3580 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SME3580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.19 | -12.5 dB |
| Peaking | 155 Hz  | 0.82 | -3.4 dB  |
| Peaking | 2239 Hz | 2    | -8.1 dB  |
| Peaking | 5234 Hz | 4.48 | -8.4 dB  |
| Peaking | 6969 Hz | 4.21 | 2.5 dB   |
| Peaking | 810 Hz  | 1.61 | 1.9 dB   |
| Peaking | 1567 Hz | 3.34 | -1.1 dB  |
| Peaking | 2168 Hz | 3.41 | 4.0 dB   |
| Peaking | 2761 Hz | 1.14 | -4.4 dB  |
| Peaking | 3500 Hz | 3.21 | 6.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SME3580/Philips%20SME3580.png)