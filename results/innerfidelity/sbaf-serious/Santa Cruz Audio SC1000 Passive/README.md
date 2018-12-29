# Santa Cruz Audio SC1000 Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.7; 54 5.4; 60 5.1; 66 4.7; 72 4.4; 79 4.0; 87 3.6; 96 3.2; 106 2.9; 116 2.7; 128 2.4; 141 2.1; 155 1.8; 170 1.7; 187 1.7; 206 1.5; 227 1.6; 249 1.5; 274 1.4; 302 1.5; 332 1.5; 365 1.5; 402 1.5; 442 1.7; 486 1.6; 535 1.6; 588 1.9; 647 1.8; 712 1.5; 783 1.4; 861 0.8; 947 0.3; 1042 -0.0; 1146 -0.2; 1261 -0.7; 1387 -1.6; 1526 -2.6; 1678 -3.4; 1846 -4.0; 2031 -4.5; 2234 -5.3; 2457 -6.0; 2703 -7.0; 2973 -7.1; 3270 -6.5; 3597 -5.9; 3957 -7.4; 4353 -11.7; 4788 -15.1; 5267 -13.2; 5793 -9.0; 6373 -7.3; 7010 -8.9; 7711 -12.3; 8482 -14.2; 9330 -12.6; 10263 -8.7; 11289 -2.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Santa Cruz Audio SC1000 Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Santa Cruz Audio SC1000 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.35 | 6.2 dB   |
| Peaking | 601 Hz   | 0.72 | 2.0 dB   |
| Peaking | 2509 Hz  | 1.06 | -5.6 dB  |
| Peaking | 4877 Hz  | 3.12 | -12.7 dB |
| Peaking | 8607 Hz  | 2.52 | -14.1 dB |
| Peaking | 2343 Hz  | 3.24 | 1.6 dB   |
| Peaking | 2970 Hz  | 1.3  | -1.6 dB  |
| Peaking | 3606 Hz  | 4.83 | 2.2 dB   |
| Peaking | 10237 Hz | 4.22 | -4.3 dB  |
| Peaking | 11836 Hz | 1.92 | 3.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Santa%20Cruz%20Audio%20SC1000%20Passive/Santa%20Cruz%20Audio%20SC1000%20Passive.png)