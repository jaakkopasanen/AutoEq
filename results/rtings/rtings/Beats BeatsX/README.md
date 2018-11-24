# Beats BeatsX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.6; 28 1.6; 31 1.6; 34 1.6; 37 1.6; 41 1.6; 45 1.6; 49 1.6; 54 1.5; 60 1.2; 66 0.9; 72 0.7; 79 0.6; 87 0.7; 96 0.7; 106 0.6; 116 0.5; 128 0.5; 141 0.4; 155 0.5; 170 0.7; 187 0.9; 206 1.1; 227 1.4; 249 1.6; 274 1.5; 302 1.6; 332 1.8; 365 2.0; 402 2.1; 442 2.2; 486 2.3; 535 2.4; 588 2.5; 647 2.5; 712 2.4; 783 1.9; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.1; 1387 -1.1; 1526 -1.0; 1678 -1.1; 1846 -1.3; 2031 -1.4; 2234 -1.1; 2457 -0.3; 2703 1.2; 2973 3.6; 3270 5.8; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.2; 5793 4.4; 6373 4.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.4; 10263 -4.9; 11289 -2.4; 12418 -2.7; 13660 -3.2; 15026 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats BeatsX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats BeatsX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.62 | 1.8 dB  |
| Peaking | 547 Hz   | 0.69 | 3.0 dB  |
| Peaking | 2236 Hz  | 0.68 | -9.2 dB |
| Peaking | 3698 Hz  | 0.64 | 12.3 dB |
| Peaking | 10635 Hz | 1.37 | -5.9 dB |
| Peaking | 763 Hz   | 2.68 | 1.0 dB  |
| Peaking | 1641 Hz  | 0.8  | -1.9 dB |
| Peaking | 1682 Hz  | 1.89 | 2.6 dB  |
| Peaking | 3239 Hz  | 6.18 | 1.6 dB  |
| Peaking | 4073 Hz  | 5.18 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beats%20BeatsX/Beats%20BeatsX.png)