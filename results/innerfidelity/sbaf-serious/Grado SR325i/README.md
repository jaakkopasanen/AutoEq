# Grado SR325i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.3; 45 4.4; 49 3.5; 54 2.5; 60 1.4; 66 0.4; 72 -0.3; 79 -1.0; 87 -1.7; 96 -2.2; 106 -2.4; 116 -2.5; 128 -2.5; 141 -2.4; 155 -2.4; 170 -2.1; 187 -1.8; 206 -1.5; 227 -1.2; 249 -1.1; 274 -0.8; 302 -0.8; 332 -0.7; 365 -0.4; 402 -0.2; 442 0.3; 486 -0.0; 535 -0.1; 588 0.3; 647 0.4; 712 0.3; 783 0.4; 861 0.2; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.8; 1387 -1.8; 1526 -3.1; 1678 -3.8; 1846 -5.3; 2031 -8.8; 2234 -7.5; 2457 -5.2; 2703 -3.5; 2973 -1.1; 3270 0.4; 3597 0.8; 3957 -2.3; 4353 -8.5; 4788 -4.8; 5267 -1.8; 5793 -1.1; 6373 -1.3; 7010 -3.7; 7711 -5.2; 8482 -7.5; 9330 -10.4; 10263 -7.5; 11289 -0.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.56 | 7.1 dB   |
| Peaking | 100 Hz   | 0.73 | -4.4 dB  |
| Peaking | 2096 Hz  | 2.65 | -8.6 dB  |
| Peaking | 9115 Hz  | 2.67 | -10.4 dB |
| Peaking | 24000 Hz | 2.3  | -7.5 dB  |
| Peaking | 744 Hz   | 1.49 | 0.8 dB   |
| Peaking | 3683 Hz  | 3.7  | 5.2 dB   |
| Peaking | 4343 Hz  | 4.41 | -10.0 dB |
| Peaking | 5586 Hz  | 4.08 | 1.5 dB   |
| Peaking | 12032 Hz | 5.03 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325i/Grado%20SR325i.png)