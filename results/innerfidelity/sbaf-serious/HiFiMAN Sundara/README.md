# HiFiMAN Sundara

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 4.4; 25 4.1; 28 3.9; 31 3.7; 34 3.6; 37 3.6; 41 3.5; 45 3.5; 49 3.5; 54 3.2; 60 2.8; 66 2.2; 72 1.9; 79 1.7; 87 1.5; 96 1.2; 106 1.0; 116 0.9; 128 0.6; 141 0.4; 155 0.3; 170 0.2; 187 0.1; 206 -0.1; 227 -0.1; 249 -0.2; 274 -0.3; 302 -0.3; 332 -0.5; 365 -0.5; 402 -0.6; 442 -0.3; 486 0.3; 535 0.5; 588 0.4; 647 -0.2; 712 -0.6; 783 -0.3; 861 -0.6; 947 -0.7; 1042 1.3; 1146 1.3; 1261 1.5; 1387 1.3; 1526 1.3; 1678 2.1; 1846 2.1; 2031 2.1; 2234 1.8; 2457 1.8; 2703 0.0; 2973 -0.0; 3270 -1.2; 3597 -0.2; 3957 -0.9; 4353 -2.5; 4788 -2.1; 5267 -1.1; 5793 -1.6; 6373 2.1; 7010 -1.2; 7711 -1.2; 8482 -2.5; 9330 -0.9; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN Sundara GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.79 | 4.4 dB  |
| Peaking | 50 Hz   |  1.06 | 2.4 dB  |
| Peaking | 1863 Hz |  1.71 | 2.4 dB  |
| Peaking | 4533 Hz |  2.98 | -2.6 dB |
| Peaking | 8514 Hz |  6.08 | -2.7 dB |
| Peaking | 327 Hz  |  2.07 | -0.6 dB |
| Peaking | 959 Hz  |  3.43 | -2.3 dB |
| Peaking | 1061 Hz |  4.14 | 2.5 dB  |
| Peaking | 3189 Hz | 10.57 | -1.4 dB |
| Peaking | 6382 Hz | 19.37 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Sundara/HiFiMAN%20Sundara.png)