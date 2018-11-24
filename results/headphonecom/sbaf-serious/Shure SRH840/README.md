# Shure SRH840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.2; 25 4.3; 28 2.9; 31 1.8; 34 0.9; 37 0.1; 41 -1.3; 45 -2.5; 49 -3.2; 54 -3.3; 60 -3.1; 66 -3.4; 72 -4.6; 79 -5.9; 87 -6.9; 96 -7.6; 106 -7.9; 116 -7.8; 128 -7.5; 141 -7.2; 155 -6.3; 170 -5.5; 187 -4.9; 206 -3.6; 227 -2.8; 249 -2.5; 274 -2.0; 302 -4.4; 332 -4.0; 365 -3.3; 402 -2.7; 442 -2.4; 486 -2.1; 535 -1.7; 588 -1.3; 647 -0.9; 712 -0.4; 783 -0.0; 861 0.2; 947 0.2; 1042 0.0; 1146 0.3; 1261 0.2; 1387 -0.3; 1526 -1.6; 1678 -3.0; 1846 -3.7; 2031 -4.2; 2234 -4.5; 2457 -4.2; 2703 -3.0; 2973 -2.6; 3270 -1.8; 3597 -1.1; 3957 -1.0; 4353 -2.2; 4788 -3.0; 5267 0.0; 5793 3.6; 6373 3.5; 7010 2.4; 7711 -1.3; 8482 -8.4; 9330 -11.2; 10263 -2.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.26 | 6.7 dB   |
| Peaking | 113 Hz   | 0.62 | -7.7 dB  |
| Peaking | 2290 Hz  | 1.64 | -4.6 dB  |
| Peaking | 6480 Hz  | 3.98 | 5.6 dB   |
| Peaking | 9029 Hz  | 4.97 | -13.1 dB |
| Peaking | 257 Hz   | 2.03 | 4.9 dB   |
| Peaking | 303 Hz   | 1.58 | -4.6 dB  |
| Peaking | 1045 Hz  | 1.87 | 1.3 dB   |
| Peaking | 4652 Hz  | 9.13 | -3.6 dB  |
| Peaking | 10923 Hz | 7.26 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)