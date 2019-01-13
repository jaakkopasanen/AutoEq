# Monster Beats Studio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 3.1; 28 -1.3; 31 -4.8; 34 -6.4; 37 -6.8; 41 -6.7; 45 -6.3; 49 -6.1; 54 -5.9; 60 -5.7; 66 -5.5; 72 -5.3; 79 -5.6; 87 -6.3; 96 -6.9; 106 -7.2; 116 -7.3; 128 -7.5; 141 -7.7; 155 -7.6; 170 -7.6; 187 -7.7; 206 -7.6; 227 -7.5; 249 -7.4; 274 -7.1; 302 -7.0; 332 -6.9; 365 -6.3; 402 -6.5; 442 -6.2; 486 -5.8; 535 -5.3; 588 -4.1; 647 -2.2; 712 -0.9; 783 0.4; 861 1.0; 947 0.6; 1042 -0.4; 1146 -1.8; 1261 -3.7; 1387 -5.4; 1526 -6.4; 1678 -7.3; 1846 -7.1; 2031 -6.3; 2234 -5.2; 2457 -3.6; 2703 -1.9; 2973 0.1; 3270 2.2; 3597 0.2; 3957 -1.0; 4353 -3.7; 4788 -5.5; 5267 -0.8; 5793 -3.1; 6373 -1.4; 7010 -1.9; 7711 -5.5; 8482 -9.1; 9330 -8.9; 10263 -4.9; 11289 -0.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Studio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.7  | 12.0 dB  |
| Peaking | 33 Hz   | 0.93 | -8.9 dB  |
| Peaking | 193 Hz  | 0.47 | -7.9 dB  |
| Peaking | 1791 Hz | 2.32 | -7.6 dB  |
| Peaking | 8823 Hz | 3.01 | -10.2 dB |
| Peaking | 504 Hz  | 2.08 | -2.6 dB  |
| Peaking | 850 Hz  | 1.89 | 3.9 dB   |
| Peaking | 1358 Hz | 3.78 | -2.3 dB  |
| Peaking | 3302 Hz | 7.37 | 3.9 dB   |
| Peaking | 4621 Hz | 8.82 | -6.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Studio/Monster%20Beats%20Studio.png)