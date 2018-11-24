# Beats BeatsX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.6; 28 1.6; 31 1.6; 34 1.6; 37 1.6; 41 1.6; 45 1.6; 49 1.6; 54 1.5; 60 1.2; 66 0.9; 72 0.7; 79 0.6; 87 0.7; 96 0.7; 106 0.6; 116 0.5; 128 0.5; 141 0.4; 155 0.5; 170 0.7; 187 0.9; 206 1.1; 227 1.4; 249 1.6; 274 1.5; 302 1.6; 332 1.8; 365 2.0; 402 2.1; 442 2.2; 486 2.3; 535 2.4; 588 2.5; 647 2.5; 712 2.4; 783 1.9; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.1; 1387 -1.1; 1526 -1.1; 1678 -1.1; 1846 -1.3; 2031 -1.4; 2234 -1.1; 2457 -0.3; 2703 1.0; 2973 3.1; 3270 5.2; 3597 5.9; 3957 5.9; 4353 5.3; 4788 4.5; 5267 2.6; 5793 1.9; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.0; 10263 -2.7; 11289 -3.3; 12418 -6.0; 13660 -6.5; 15026 -0.8; 16529 0.0; 18182 -0.1; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats BeatsX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats BeatsX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.45 | 1.7 dB  |
| Peaking | 459 Hz   | 1.09 | 2.6 dB  |
| Peaking | 3920 Hz  | 2.47 | 6.7 dB  |
| Peaking | 6591 Hz  | 5.66 | 3.5 dB  |
| Peaking | 12895 Hz | 2.66 | -7.4 dB |
| Peaking | 731 Hz   | 2.53 | 1.8 dB  |
| Peaking | 1947 Hz  | 0.6  | -2.1 dB |
| Peaking | 3206 Hz  | 4.43 | 3.2 dB  |
| Peaking | 4808 Hz  | 6.51 | 2.0 dB  |
| Peaking | 19920 Hz | 4.89 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20BeatsX/Beats%20BeatsX.png)