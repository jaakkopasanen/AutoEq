# T-Peos Altone 200 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -2.6; 23 -3.1; 25 -3.6; 28 -4.2; 31 -4.6; 34 -5.0; 37 -5.3; 41 -5.7; 45 -6.0; 49 -6.3; 54 -6.6; 60 -7.0; 66 -7.2; 72 -7.5; 79 -7.8; 87 -8.1; 96 -8.3; 106 -8.4; 116 -8.3; 128 -8.3; 141 -8.2; 155 -8.0; 170 -7.8; 187 -7.4; 206 -7.0; 227 -6.5; 249 -6.1; 274 -5.5; 302 -4.9; 332 -4.3; 365 -3.6; 402 -3.1; 442 -2.3; 486 -1.8; 535 -1.2; 588 -0.4; 647 0.0; 712 0.2; 783 0.7; 861 0.5; 947 0.3; 1042 -0.1; 1146 -0.6; 1261 -1.1; 1387 -2.1; 1526 -3.2; 1678 -4.3; 1846 -5.3; 2031 -5.9; 2234 -6.3; 2457 -5.1; 2703 -4.1; 2973 -2.8; 3270 -2.6; 3597 -2.6; 3957 -2.4; 4353 -1.6; 4788 -0.1; 5267 0.4; 5793 -0.1; 6373 -1.8; 7010 -4.3; 7711 -4.3; 8482 -5.7; 9330 -8.4; 10263 -8.5; 11289 -4.6; 12418 -0.4; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Altone 200 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Altone 200 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.47 | -6.0 dB |
| Peaking | 144 Hz   | 0.93 | -4.7 dB |
| Peaking | 270 Hz   | 1.58 | -2.8 dB |
| Peaking | 2156 Hz  | 1.77 | -6.3 dB |
| Peaking | 9589 Hz  | 2.48 | -9.3 dB |
| Peaking | 819 Hz   | 2.49 | 1.7 dB  |
| Peaking | 4033 Hz  | 2.93 | -1.8 dB |
| Peaking | 5283 Hz  | 2.47 | 2.4 dB  |
| Peaking | 6980 Hz  | 5.32 | -2.6 dB |
| Peaking | 13106 Hz | 4.29 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Altone%20200%202014/T-Peos%20Altone%20200%202014.png)