# AKG K391-NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.7; 28 1.5; 31 1.2; 34 1.1; 37 1.0; 41 0.9; 45 0.8; 49 0.8; 54 0.7; 60 0.5; 66 0.3; 72 0.1; 79 -0.0; 87 -0.2; 96 -0.4; 106 -0.7; 116 -1.1; 128 -1.4; 141 -1.7; 155 -2.0; 170 -2.3; 187 -2.6; 206 -3.0; 227 -3.5; 249 -3.9; 274 -4.4; 302 -4.8; 332 -5.2; 365 -5.6; 402 -5.9; 442 -5.9; 486 -5.7; 535 -5.2; 588 -4.2; 647 -2.8; 712 -1.4; 783 -0.1; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.8; 1387 -0.9; 1526 -0.7; 1678 -0.5; 1846 -0.3; 2031 0.1; 2234 1.0; 2457 1.9; 2703 1.8; 2973 0.6; 3270 -1.4; 3597 -3.6; 3957 -5.5; 4353 -6.2; 4788 -4.1; 5267 -1.1; 5793 1.5; 6373 2.2; 7010 2.1; 7711 0.2; 8482 -4.1; 9330 -7.4; 10263 -5.4; 11289 -0.5; 12418 0.0; 13660 0.0; 15026 -1.3; 16529 -0.8; 18182 0.0; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K391-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K391-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.6  | 2.4 dB   |
| Peaking | 372 Hz   | 0.87 | -6.1 dB  |
| Peaking | 4284 Hz  | 2.12 | -12.9 dB |
| Peaking | 5323 Hz  | 0.66 | 7.1 dB   |
| Peaking | 9414 Hz  | 2.92 | -10.8 dB |
| Peaking | 548 Hz   | 3.54 | -1.5 dB  |
| Peaking | 842 Hz   | 2.19 | 2.5 dB   |
| Peaking | 1760 Hz  | 0.8  | -1.4 dB  |
| Peaking | 2562 Hz  | 3.43 | 2.5 dB   |
| Peaking | 15565 Hz | 4.27 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K391-NC/AKG%20K391-NC.png)