# Denon AH-C260R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 21 -15.1; 23 -15.1; 25 -15.0; 28 -14.9; 31 -14.8; 34 -14.6; 37 -14.5; 41 -14.3; 45 -14.1; 49 -13.9; 54 -13.7; 60 -13.5; 66 -13.3; 72 -13.2; 79 -13.0; 87 -12.8; 96 -12.4; 106 -12.1; 116 -11.7; 128 -11.4; 141 -11.0; 155 -10.6; 170 -10.1; 187 -9.6; 206 -9.0; 227 -8.3; 249 -7.7; 274 -7.0; 302 -6.3; 332 -5.6; 365 -4.8; 402 -4.0; 442 -3.4; 486 -2.8; 535 -2.2; 588 -1.5; 647 -0.8; 712 -0.4; 783 0.0; 861 0.2; 947 0.1; 1042 -0.2; 1146 -0.5; 1261 -0.8; 1387 -1.5; 1526 -2.1; 1678 -2.6; 1846 -2.7; 2031 -2.8; 2234 -2.9; 2457 -2.9; 2703 -3.3; 2973 -3.7; 3270 -2.7; 3597 -1.2; 3957 -1.4; 4353 -3.2; 4788 -4.5; 5267 -5.2; 5793 -6.3; 6373 -5.0; 7010 -2.9; 7711 -1.6; 8482 -1.3; 9330 -2.9; 10263 -3.7; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.2; 18182 -1.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C260R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-2**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C260R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.18 | -14.8 dB |
| Peaking | 178 Hz   | 0.68 | -4.3 dB  |
| Peaking | 2356 Hz  | 1.55 | -3.0 dB  |
| Peaking | 5756 Hz  | 1.95 | -5.8 dB  |
| Peaking | 17862 Hz | 4.14 | -1.9 dB  |
| Peaking | 836 Hz   | 2.15 | 1.5 dB   |
| Peaking | 1611 Hz  | 4.71 | -1.1 dB  |
| Peaking | 7942 Hz  | 3.58 | 1.1 dB   |
| Peaking | 10025 Hz | 4.03 | -4.6 dB  |
| Peaking | 11245 Hz | 2.49 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C260R/Denon%20AH-C260R.png)