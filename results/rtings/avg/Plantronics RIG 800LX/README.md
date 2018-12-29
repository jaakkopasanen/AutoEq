# Plantronics RIG 800LX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 21 0.0; 23 0.6; 25 -0.3; 28 -1.4; 31 -2.1; 34 -2.5; 37 -2.7; 41 -2.8; 45 -2.6; 49 -2.4; 54 -2.0; 60 -1.6; 66 -1.4; 72 -1.3; 79 -1.3; 87 -1.2; 96 -1.3; 106 -1.3; 116 -1.3; 128 -1.3; 141 -1.2; 155 -1.0; 170 -0.7; 187 -0.3; 206 0.3; 227 0.8; 249 1.2; 274 1.5; 302 1.5; 332 1.4; 365 1.5; 402 1.4; 442 1.4; 486 1.2; 535 1.3; 588 1.4; 647 1.3; 712 1.0; 783 0.7; 861 0.1; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.8; 1387 2.0; 1526 2.2; 1678 1.8; 1846 -0.1; 2031 -1.6; 2234 -1.7; 2457 -1.4; 2703 -2.1; 2973 -4.0; 3270 -5.8; 3597 -6.5; 3957 -5.7; 4353 -4.2; 4788 -1.6; 5267 -0.3; 5793 -0.5; 6373 1.8; 7010 -1.0; 7711 -1.8; 8482 -2.1; 9330 -2.2; 10263 -2.4; 11289 -2.7; 12418 -2.1; 13660 -2.6; 15026 -5.7; 16529 -6.5; 18182 -4.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics RIG 800LX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics RIG 800LX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 64 Hz    | 0.46 | -2.4 dB |
| Peaking | 920 Hz   | 0.11 | 1.4 dB  |
| Peaking | 3507 Hz  | 1.98 | -7.7 dB |
| Peaking | 16567 Hz | 0.77 | -5.8 dB |
| Peaking | 20090 Hz | 2.71 | -3.6 dB |
| Peaking | 1001 Hz  | 2.7  | -1.8 dB |
| Peaking | 1635 Hz  | 1.78 | 2.2 dB  |
| Peaking | 2002 Hz  | 4.08 | -3.1 dB |
| Peaking | 6427 Hz  | 6.15 | 2.9 dB  |
| Peaking | 8061 Hz  | 2.45 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20RIG%20800LX/Plantronics%20RIG%20800LX.png)