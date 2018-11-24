# Ultrasone PRO 900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.0; 28 0.1; 31 -0.8; 34 -1.5; 37 -2.1; 41 -2.7; 45 -2.6; 49 -2.5; 54 -2.9; 60 -3.3; 66 -4.0; 72 -4.8; 79 -5.5; 87 -6.1; 96 -6.6; 106 -7.0; 116 -7.2; 128 -7.1; 141 -7.0; 155 -6.9; 170 -6.1; 187 -5.8; 206 -4.2; 227 -2.4; 249 -0.1; 274 2.6; 302 1.4; 332 -1.2; 365 -2.4; 402 -3.0; 442 -2.8; 486 -1.7; 535 1.2; 588 -0.2; 647 -1.3; 712 -1.1; 783 -0.9; 861 -0.8; 947 -0.3; 1042 0.3; 1146 1.2; 1261 1.2; 1387 -0.2; 1526 -1.1; 1678 -1.9; 1846 -1.9; 2031 0.1; 2234 1.4; 2457 -2.5; 2703 -4.6; 2973 -5.3; 3270 -5.5; 3597 -6.2; 3957 -7.4; 4353 -8.3; 4788 -8.4; 5267 -6.9; 5793 -8.5; 6373 -7.5; 7010 -4.8; 7711 -2.3; 8482 -0.2; 9330 0.0; 10263 0.0; 11289 -0.1; 12418 -4.4; 13660 -9.3; 15026 -11.9; 16529 -10.7; 18182 -7.9; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 96 Hz    |  1.12 | -6.3 dB  |
| Peaking | 159 Hz   |  2.47 | -4.6 dB  |
| Peaking | 418 Hz   |  5.81 | -2.9 dB  |
| Peaking | 4550 Hz  |  1.35 | -8.7 dB  |
| Peaking | 16279 Hz |  1.32 | -12.4 dB |
| Peaking | 19 Hz    |  2.9  | 2.4 dB   |
| Peaking | 280 Hz   |  7.53 | 4.6 dB   |
| Peaking | 2180 Hz  | 10.4  | 4.3 dB   |
| Peaking | 10036 Hz |  1.93 | 5.7 dB   |
| Peaking | 19514 Hz |  0.08 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)