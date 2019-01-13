# RHA SA950i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.5; 23 -5.9; 25 -6.2; 28 -6.6; 31 -6.8; 34 -6.9; 37 -6.9; 41 -7.0; 45 -6.9; 49 -6.9; 54 -6.8; 60 -6.8; 66 -6.8; 72 -6.8; 79 -6.9; 87 -6.9; 96 -6.7; 106 -7.0; 116 -6.9; 128 -7.0; 141 -7.4; 155 -7.7; 170 -7.4; 187 -7.7; 206 -7.6; 227 -7.3; 249 -7.2; 274 -7.2; 302 -7.3; 332 -7.6; 365 -7.8; 402 -7.8; 442 -7.6; 486 -7.6; 535 -7.2; 588 -6.3; 647 -5.5; 712 -4.1; 783 -2.5; 861 -1.2; 947 -0.6; 1042 -0.1; 1146 -1.1; 1261 -3.2; 1387 -5.1; 1526 -5.9; 1678 -5.6; 1846 -4.1; 2031 -2.0; 2234 -0.5; 2457 1.1; 2703 2.3; 2973 3.2; 3270 4.6; 3597 4.3; 3957 5.8; 4353 6.0; 4788 2.4; 5267 -2.1; 5793 1.5; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA SA950i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA SA950i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.25 | -6.5 dB |
| Peaking | 229 Hz  | 0.72 | -4.5 dB |
| Peaking | 483 Hz  | 1.57 | -5.4 dB |
| Peaking | 1616 Hz | 2.89 | -6.7 dB |
| Peaking | 3736 Hz | 1.55 | 5.7 dB  |
| Peaking | 656 Hz  | 6.04 | -1.2 dB |
| Peaking | 993 Hz  | 4.69 | 2.2 dB  |
| Peaking | 4538 Hz | 4.97 | 6.3 dB  |
| Peaking | 5221 Hz | 2.71 | -8.0 dB |
| Peaking | 6261 Hz | 4.98 | 7.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20SA950i/RHA%20SA950i.png)