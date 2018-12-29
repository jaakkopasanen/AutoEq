# RHA T20 Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -5.1; 23 -5.3; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.1; 41 -6.1; 45 -6.2; 49 -6.2; 54 -6.3; 60 -6.3; 66 -6.3; 72 -6.3; 79 -6.3; 87 -6.4; 96 -6.3; 106 -6.2; 116 -6.0; 128 -5.8; 141 -5.5; 155 -5.3; 170 -5.0; 187 -4.6; 206 -4.2; 227 -3.7; 249 -3.3; 274 -2.8; 302 -2.3; 332 -1.8; 365 -1.3; 402 -0.9; 442 -0.4; 486 -0.2; 535 0.2; 588 0.8; 647 1.0; 712 1.0; 783 1.2; 861 0.9; 947 0.4; 1042 -0.2; 1146 -0.9; 1261 -1.7; 1387 -3.2; 1526 -4.3; 1678 -3.3; 1846 -0.2; 2031 -2.5; 2234 -3.4; 2457 -4.5; 2703 -4.8; 2973 -3.6; 3270 -2.2; 3597 -2.0; 3957 -3.9; 4353 -8.3; 4788 -8.8; 5267 -2.8; 5793 2.4; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T20 Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.36 | -6.0 dB  |
| Peaking | 147 Hz  | 0.9  | -3.2 dB  |
| Peaking | 2411 Hz | 1.34 | -3.8 dB  |
| Peaking | 4641 Hz | 4.6  | -10.3 dB |
| Peaking | 6269 Hz | 4.07 | 6.7 dB   |
| Peaking | 744 Hz  | 1.65 | 2.0 dB   |
| Peaking | 1562 Hz | 3.12 | -3.9 dB  |
| Peaking | 1857 Hz | 5.06 | 4.1 dB   |
| Peaking | 3150 Hz | 1.86 | -1.7 dB  |
| Peaking | 3417 Hz | 4.27 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Reference%20Filter/RHA%20T20%20Reference%20Filter.png)