# Philips SHE3590
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 21 -11.2; 23 -11.1; 25 -10.9; 28 -10.7; 31 -10.4; 34 -10.2; 37 -9.9; 41 -9.6; 45 -9.3; 49 -9.1; 54 -8.8; 60 -8.5; 66 -8.3; 72 -8.1; 79 -7.9; 87 -7.8; 96 -7.6; 106 -7.2; 116 -6.9; 128 -6.6; 141 -6.3; 155 -6.0; 170 -5.5; 187 -5.1; 206 -4.7; 227 -4.0; 249 -3.6; 274 -3.1; 302 -2.6; 332 -2.1; 365 -1.6; 402 -1.2; 442 -0.7; 486 -0.4; 535 -0.1; 588 0.4; 647 0.6; 712 0.5; 783 0.7; 861 0.7; 947 0.4; 1042 -0.2; 1146 -0.8; 1261 -1.6; 1387 -2.7; 1526 -3.9; 1678 -4.8; 1846 -5.6; 2031 -6.4; 2234 -7.6; 2457 -8.4; 2703 -7.7; 2973 -4.2; 3270 -0.5; 3597 1.1; 3957 0.7; 4353 -1.9; 4788 -4.2; 5267 -5.4; 5793 -3.8; 6373 -1.8; 7010 -0.1; 7711 0.3; 8482 0.0; 9330 -0.0; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE3590 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE3590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.21 | -10.9 dB |
| Peaking | 147 Hz  | 0.87 | -3.1 dB  |
| Peaking | 2431 Hz | 1.62 | -9.4 dB  |
| Peaking | 3567 Hz | 3.08 | 5.6 dB   |
| Peaking | 5200 Hz | 3.89 | -5.4 dB  |
| Peaking | 290 Hz  | 1.63 | -0.8 dB  |
| Peaking | 872 Hz  | 0.84 | 2.1 dB   |
| Peaking | 1650 Hz | 1.29 | -2.3 dB  |
| Peaking | 2151 Hz | 3.93 | 1.7 dB   |
| Peaking | 7433 Hz | 6.25 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SHE3590/Philips%20SHE3590.png)