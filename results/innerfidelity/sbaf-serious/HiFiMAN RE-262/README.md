# HiFiMAN RE-262
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.8; 34 5.7; 37 5.6; 41 5.4; 45 5.2; 49 5.1; 54 4.9; 60 4.6; 66 4.1; 72 3.7; 79 3.4; 87 2.9; 96 2.5; 106 2.2; 116 1.8; 128 1.4; 141 1.1; 155 0.8; 170 0.6; 187 0.5; 206 0.2; 227 0.1; 249 -0.0; 274 -0.1; 302 -0.2; 332 -0.2; 365 -0.2; 402 -0.1; 442 -0.0; 486 -0.1; 535 0.0; 588 0.5; 647 0.7; 712 0.8; 783 1.2; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.3; 1261 -2.7; 1387 -4.3; 1526 -6.0; 1678 -6.7; 1846 -5.3; 2031 -2.4; 2234 0.7; 2457 4.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-262 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-262 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.6  | 5.6 dB   |
| Peaking | 62 Hz   | 0.96 | 2.5 dB   |
| Peaking | 827 Hz  | 2.72 | 1.5 dB   |
| Peaking | 1688 Hz | 1.83 | -10.9 dB |
| Peaking | 3261 Hz | 0.75 | 8.4 dB   |
| Peaking | 313 Hz  | 1.68 | -0.5 dB  |
| Peaking | 2641 Hz | 6.01 | 2.2 dB   |
| Peaking | 3361 Hz | 1.59 | -1.2 dB  |
| Peaking | 6230 Hz | 2.1  | 5.6 dB   |
| Peaking | 7445 Hz | 1.47 | -4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-262/HiFiMAN%20RE-262.png)