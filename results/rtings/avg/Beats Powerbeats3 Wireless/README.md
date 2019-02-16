# Beats Powerbeats3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 -5.1; 23 -5.2; 25 -5.3; 28 -5.5; 31 -5.6; 34 -5.7; 37 -5.7; 41 -5.8; 45 -5.8; 49 -5.7; 54 -5.7; 60 -5.8; 66 -5.9; 72 -5.9; 79 -5.9; 87 -5.9; 96 -6.0; 106 -6.0; 116 -6.0; 128 -6.0; 141 -5.9; 155 -5.8; 170 -5.6; 187 -5.3; 206 -4.9; 227 -4.6; 249 -4.1; 274 -3.7; 302 -3.3; 332 -3.0; 365 -2.7; 402 -2.3; 442 -1.8; 486 -1.6; 535 -1.8; 588 -2.0; 647 -2.3; 712 -2.8; 783 -3.0; 861 -3.3; 947 -4.0; 1042 -4.8; 1146 -5.5; 1261 -6.2; 1387 -6.6; 1526 -6.8; 1678 -6.8; 1846 -6.7; 2031 -6.6; 2234 -6.2; 2457 -5.0; 2703 -3.5; 2973 -2.0; 3270 -1.0; 3597 -0.9; 3957 -1.5; 4353 -2.8; 4788 -4.5; 5267 -5.2; 5793 -2.1; 6373 -0.5; 7010 -1.9; 7711 -4.2; 8482 -4.4; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 137 Hz  | 0.28 | -2.1 dB |
| Peaking | 550 Hz  | 0.59 | 5.1 dB  |
| Peaking | 2150 Hz | 0.44 | -5.1 dB |
| Peaking | 3336 Hz | 1.65 | 7.8 dB  |
| Peaking | 6471 Hz | 4.53 | 5.3 dB  |
| Peaking | 5106 Hz | 6.18 | -2.9 dB |
| Peaking | 5118 Hz | 2.46 | 1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Powerbeats3%20Wireless/Beats%20Powerbeats3%20Wireless.png)