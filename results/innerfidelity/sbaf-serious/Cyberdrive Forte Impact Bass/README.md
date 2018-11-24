# Cyberdrive Forte Impact Bass

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 -9.8; 23 -9.8; 25 -9.8; 28 -9.8; 31 -9.8; 34 -9.8; 37 -9.8; 41 -9.8; 45 -9.7; 49 -9.7; 54 -9.7; 60 -9.7; 66 -9.7; 72 -9.7; 79 -9.8; 87 -9.8; 96 -9.8; 106 -9.7; 116 -9.5; 128 -9.3; 141 -9.1; 155 -8.8; 170 -8.5; 187 -8.1; 206 -7.7; 227 -7.1; 249 -6.7; 274 -6.2; 302 -5.7; 332 -5.1; 365 -4.6; 402 -4.0; 442 -3.4; 486 -2.9; 535 -2.4; 588 -1.7; 647 -1.2; 712 -0.8; 783 -0.3; 861 -0.1; 947 -0.1; 1042 0.3; 1146 0.6; 1261 0.4; 1387 0.3; 1526 0.3; 1678 0.5; 1846 1.1; 2031 2.0; 2234 2.8; 2457 4.1; 2703 4.7; 2973 5.3; 3270 5.3; 3597 3.9; 3957 1.4; 4353 -1.8; 4788 -3.4; 5267 -4.0; 5793 -6.8; 6373 -11.1; 7010 -7.8; 7711 -3.8; 8482 -1.7; 9330 -2.6; 10263 -4.4; 11289 -1.5; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.7; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cyberdrive Forte Impact Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyberdrive Forte Impact Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.17 | -10.3 dB |
| Peaking | 3370 Hz  | 1.14 | 7.4 dB   |
| Peaking | 4504 Hz  | 2.58 | -5.7 dB  |
| Peaking | 6422 Hz  | 3.3  | -12.0 dB |
| Peaking | 10290 Hz | 5.94 | -4.3 dB  |
| Peaking | 16 Hz    | 1.16 | -1.3 dB  |
| Peaking | 51 Hz    | 0.87 | 1.0 dB   |
| Peaking | 252 Hz   | 0.35 | -0.7 dB  |
| Peaking | 850 Hz   | 0.66 | 1.3 dB   |
| Peaking | 1643 Hz  | 2.36 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cyberdrive%20Forte%20Impact%20Bass/Cyberdrive%20Forte%20Impact%20Bass.png)